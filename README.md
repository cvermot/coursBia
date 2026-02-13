# Cours BIA
[![Compilation LaTeX - Cours complet](https://github.com/cvermot/coursBia/actions/workflows/compilLatex.yml/badge.svg)](https://github.com/cvermot/coursBia/actions/workflows/compilLatex.yml)
[![Compilation LaTeX - Nightly](https://github.com/cvermot/coursBia/actions/workflows/nightly.yml/badge.svg)](https://github.com/cvermot/coursBia/actions/workflows/nightly.yml)

[![Licence: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Ce dépot contient un cours BIA destiné à des élèves de troisième/seconde.

Travail en cours.

## Génération LaTeX
Le cours est produit avec l'outil LaTeX.

La compilation se fait avec un environnement LaTeX standard, cependant il faut tenir compte des paramètres suivants :
- pour améliorer la vitesse de compilation sur la machine de développement, il est possible de réaliser la compilation en mode externe :
  - Si ce mode reste actif, la compilation initiale sera très longue, mais les suivantes plus rapides
  - Il faut impérativement passer l'option `-shell-escape` à votre compilateur LaTeX
  - Si vous souhaitez compiler en mode externe, il suffit de décommenter la ligne `\tikzexternalize` dans le fichier `param/external.tex`
- la bibliographie utilise `biber`. La préparation de l'environnement bibliographique se fait donc avec la commande `biber`.

A noter : dans certaines configurations, la compilation peut entrainer le dépassement de la mémoire allouée à TeX. Dans ce cas, le recours à LuaTeX permet généralement de contourner le problème.

### Compilation
#### Compilation rapide
Le projet est fourni avec un fichier de configuration latexmk. On peut compiler l'ensemble en tapant simplement :
```
latexmk CoursBIA_complet.tex
```

#### Compilation détaillée
Les commandes à exécuter pour compiler le projet :

```
pdflatex -shell-escape CoursBIA_complet.tex
makeindex %.glo -t %.glg -s %.ist -o %.gls
biber CoursBIA_complet.bcf
pdflatex -shell-escape CoursBIA_complet.tex
pdflatex -shell-escape CoursBIA_complet.tex
```

## Utilitaires Python

Le dépôt contient des utilitaires Python pour le traitement de données :

### Suppression des caractères Unicode d'espacement

Pour supprimer le caractère `\u2002` (EN SPACE) et d'autres espaces Unicode dans des chaînes de caractères :

```bash
python3 example_simple.py          # Exemple simple
python3 remove_unicode_spaces.py   # Démonstration complète
python3 test_remove_unicode_spaces.py  # Tests unitaires
```

Voir le [guide de suppression des espaces Unicode](UNICODE_SPACES_GUIDE.md) pour plus de détails.

