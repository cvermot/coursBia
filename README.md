# Cours BIA
[![Compilation LaTeX - Cours complet](https://github.com/cvermot/coursBia/actions/workflows/compilLatex.yml/badge.svg)](https://github.com/cvermot/coursBia/actions/workflows/compilLatex.yml)

Ce dépot contient un cours BIA destiné à des élèves de troisième/seconde.

Travail en cours.

## Génération LaTeX
Le cours produit avec l'outil LaTeX.

La compilation se fait avec un environement LaTeX standard, cependant il faut tenir compte des paramètres suivants :
- pour améliorer la vitesse de compilation, la génération des animations TikZ est réalisée par défaut en mode externe :
  - Si ce mode reste actif, la compilation initiale sera très longue, mais les suivantes plus rapides
  - Il faut impérativement passer l'option `-shell-escape` à votre compilateur LaTeX
  - Si vous souhaitez compiler en mode non externe, il suffit de commenter la ligne `\tikzexternalize` dans la préambule du fichier `CoursBIA_complet.tex`
- la bibliographie utilise `biber`. La préparation de l'environnement bibliographique se fait donc avec la commande `biber`.

A noter : dans certaines configrations, la compilation peut entrainer le dépassement de la mémoire allouée à TeX. Dans ce cas, le recours à LuaTeX permet généralement de contourner le problème.

### Compilation
Les commandes à exécuter pour 

```
pdflatex -shell-escape CoursBIA_complet.tex
makeindex %.glo -t %.glg -s %.ist -o %.gls
biber CoursBIA_complet.bcf
pdflatex -shell-escape CoursBIA_complet.tex
pdflatex -shell-escape CoursBIA_complet.tex
```

