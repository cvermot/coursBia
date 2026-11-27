import re
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


class BibliographieExtraitsTest(unittest.TestCase):
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
                log = Path(output, f"{document}.log").read_text(encoding="latin-1")
                self.assertNotRegex(log, r"Citation '.*' .* undefined")


if __name__ == "__main__":
    unittest.main()
