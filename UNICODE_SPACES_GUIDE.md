# Guide de suppression du caractère \u2002 en Python

## Problème

Comment retirer le caractère `\u2002` (EN SPACE) dans une chaîne comme `"0;\"&gt;Unknown\u2002"` en Python ?

## Solutions

### Solution 1 : Méthode replace() simple

La méthode la plus directe pour supprimer le caractère `\u2002` :

```python
# Chaîne avec le caractère \u2002
s = '0;"&gt;Unknown\u2002'

# Suppression du caractère \u2002
s_clean = s.replace('\u2002', '')

print(repr(s_clean))  # '0;"&gt;Unknown'
```

### Solution 2 : Utiliser le script fourni

Un script utilitaire `remove_unicode_spaces.py` est fourni avec plusieurs fonctions :

```python
from remove_unicode_spaces import remove_en_space

s = '0;"&gt;Unknown\u2002'
s_clean = remove_en_space(s)
print(s_clean)  # 0;"&gt;Unknown
```

### Solution 3 : Suppression de tous les espaces Unicode

Pour supprimer tous les types d'espaces Unicode :

```python
from remove_unicode_spaces import remove_all_unicode_spaces

s = 'Texte avec\u2002plusieurs\u2003types\u2009d\'espaces'
s_clean = remove_all_unicode_spaces(s)
print(s_clean)  # Texte avecplusieurstypesd'espaces
```

### Solution 4 : Normalisation des espaces Unicode

Pour remplacer les espaces Unicode par des espaces standards :

```python
from remove_unicode_spaces import normalize_spaces

s = 'Texte avec\u2002espaces\u2003spéciaux'
s_normalized = normalize_spaces(s)
print(s_normalized)  # Texte avec espaces spéciaux
```

## Caractères Unicode d'espacement

Voici les principaux caractères d'espacement Unicode :

| Code     | Nom                      | Caractère |
|----------|--------------------------|-----------|
| U+2002   | EN SPACE                 | ` `       |
| U+2003   | EM SPACE                 | ` `       |
| U+2009   | THIN SPACE               | ` `       |
| U+200A   | HAIR SPACE               | ` `       |
| U+202F   | NARROW NO-BREAK SPACE    | ` `       |

## Utilisation du script

### Ligne de commande

```bash
python3 remove_unicode_spaces.py
```

Cela affichera des exemples de démonstration.

### En tant que module

```python
import remove_unicode_spaces

# Supprimer \u2002 uniquement
text = '0;"&gt;Unknown\u2002'
clean_text = remove_unicode_spaces.remove_en_space(text)

# Supprimer tous les espaces Unicode
clean_text = remove_unicode_spaces.remove_all_unicode_spaces(text)

# Normaliser les espaces
normal_text = remove_unicode_spaces.normalize_spaces(text)
```

## Cas d'usage dans ce projet

Ce type de nettoyage peut être utile pour :
- Traiter des données exportées de GeoGebra
- Nettoyer des chaînes XML
- Préparer du texte pour LaTeX
- Normaliser des données CSV

## Références

- [Unicode Space Characters](https://en.wikipedia.org/wiki/Whitespace_character#Unicode)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
