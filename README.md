# Cours BIA
[![Compilation LaTeX - Cours complet](https://github.com/cvermot/coursBia/actions/workflows/compilLatex.yml/badge.svg)](https://github.com/cvermot/coursBia/actions/workflows/compilLatex.yml)
[![Compilation LaTeX - Nightly](https://github.com/cvermot/coursBia/actions/workflows/nightly.yml/badge.svg)](https://github.com/cvermot/coursBia/actions/workflows/nightly.yml)
[![Compilation LaTeX - Release](https://github.com/cvermot/coursBia/actions/workflows/release.yml/badge.svg)](https://github.com/cvermot/coursBia/actions/workflows/release.yml)
[![Compilation LaTeX - Compilation des présentations](https://github.com/cvermot/coursBia/actions/workflows/compilPresentations.yml/badge.svg)](https://github.com/cvermot/coursBia/actions/workflows/compilPresentations.yml)

[![Licence: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Ce dépot contient un cours BIA destiné à des élèves de troisième/seconde. Consultez [brevet.initiation.aero](https://brevet.initiation.aero/) pour disposer de l'ensemble des informations.

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

Avec LuaLaTeX, les icônes des encadrés utilisent la police Font Awesome 7 fournie dans `fonts/`. Avec pdfLaTeX, elles utilisent les icônes Font Awesome 5 du package pour préserver la compatibilité.

### Images extraites d'un livre

Pour une image issue d'un chapitre, utiliser une entrée `@misc` de sous-type `imageextrait`, reliée par `crossref` à une entrée `@inbook`, elle-même reliée au livre. Le chapitre sert uniquement à partager les données de source : `options = {dataonly=true}` évite son affichage et sa numérotation comme notice distincte, y compris avec `\nocite{*}`.

```bibtex
@book{livre,
  author = {Auteur, Prénom},
  title = {Titre du livre},
  year = {2023},
  note = {Licence : domaine public}
}
@inbook{chapitre,
  crossref = {livre},
  title = {Chapitre 1 : Titre du chapitre},
  options = {dataonly=true}
}
@misc{img:exemple,
  entrysubtype = {imageextrait},
  crossref = {chapitre},
  title = {Titre de l'image},
  pages = {1.7},
  xdata = {tradCvd}
}
```

Le champ `xdata` est facultatif ; `tradCvd` indique une traduction par Clément Vermot-Desroches. La notice de l'image renvoie par un numéro à la notice du livre, où figurent notamment la licence, l'URL et la date de consultation. Si seule l'image est citée, cette citation du livre est découverte à l'impression de la bibliographie : un passage supplémentaire de Biber et de LaTeX peut être nécessaire. `latexmk` effectue les passages nécessaires.

Les exemples de vérification se compilent depuis la racine avec `latexmk -pdf tests/bibliographie-extraits.tex` et `latexmk -pdf tests/bibliographie-extraits-beamer.tex`.

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

