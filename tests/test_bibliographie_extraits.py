import re
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


class BibliographieExtraitsTest(unittest.TestCase):
    def test_toutes_les_images_extraites_sont_converties(self):
        entries = {}
        source_notes = []
        for path in ROOT.rglob("*.bib"):
            if ".git" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            source_notes.extend(
                re.findall(r"Schéma issu de \\cite\{faa[^}]+\}", text)
            )
            source_notes.extend(re.findall(r"Image extraite du magasine", text))
            for entry in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", text, re.S):
                entries[entry.group(2).strip()] = (entry.group(1).lower(), entry.group(3))

        extracted = {
            key: body
            for key, (kind, body) in entries.items()
            if kind == "misc" and re.search(r"entrysubtype\s*=\s*\{imageextrait\}", body)
        }
        self.assertGreaterEqual(len(extracted), 70)
        self.assertEqual(source_notes, [])
        for key, body in extracted.items():
            crossref = re.search(r"crossref\s*=\s*\{([^}]+)\}", body)
            self.assertIsNotNone(crossref, key)
            parent_type, _ = entries[crossref.group(1)]
            self.assertIn(parent_type, {"book", "inbook"}, key)
            self.assertRegex(body, r"pages\s*=", key)
            if parent_type == "book":
                self.assertRegex(body, rf"userb\s*=\s*\{{{re.escape(crossref.group(1))}\}}", key)

    def test_titre_et_renvoi_du_livre(self):
        for document in ("bibliographie-extraits", "bibliographie-extraits-beamer"):
            with self.subTest(document=document), tempfile.TemporaryDirectory() as output:
                subprocess.run(
                    [
                        "latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
                        f"-outdir={output}", f"tests/{document}.tex",
                    ],
                    cwd=ROOT, check=True, stdout=subprocess.DEVNULL,
                )
                text = subprocess.check_output(
                    ["pdftotext", "-layout", f"{output}/{document}.pdf", "-"],
                    text=True,
                )
                text = " ".join(text.split())
                notice = text.split("Forces et contraintes", 1)[1]
                self.assertRegex(
                    notice,
                    r"extrait de Aviation Maintenance Technician Handbook - Airframe"
                    r"\s+\[\d+\], Chapitre 1\s*: Aircraft Structures, p\. 1\.7",
                )
                self.assertRegex(notice, r"Vermot-Desroches")
                self.assertNotRegex(
                    notice.split("Vermot-Desroches", 1)[0],
                    r"Licence|https?://|Oklahoma|2023",
                )
                if document == "bibliographie-extraits":
                    self.assertIn("Aviation Maintenance Technician Handbook - Airframe", text)
                    self.assertIn("Aviation Maintenance Technician Handbook - Powerplant", text)
                    self.assertIn("Pilot's Handbook of Aeronautical Knowledge", text)
                    self.assertIn("Info Pilote n°828", text)
                    self.assertRegex(
                        text,
                        r"Denis Capdegelle, Répartition des nuages dans la troposphère,"
                        r"\s+extrait de Info Pilote n°828\s+\[\d+\], p\. 48",
                    )
                    self.assertIn("Tous droits réservés, Info Pilote", text)
                log = Path(output, f"{document}.log").read_text(encoding="latin-1")
                self.assertNotRegex(log, r"Citation '.*' .* undefined")


if __name__ == "__main__":
    unittest.main()
