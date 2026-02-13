#!/usr/bin/env python3
"""
Quick reference example for removing \u2002 character.

This file provides the simplest solution to the problem:
"En python comment retirer \u2002 dans la chaine \"0;\"&gt;Unknown\u2002"
"""

# ============================================
# SOLUTION SIMPLE / SIMPLE SOLUTION
# ============================================

# Chaîne avec le caractère \u2002
text = '0;"&gt;Unknown\u2002'

# Méthode 1: Utiliser replace() directement
cleaned_text = text.replace('\u2002', '')

print(f"Original: {repr(text)}")
print(f"Nettoyé:  {repr(cleaned_text)}")

# ============================================
# SOLUTION AVEC FONCTION / FUNCTION SOLUTION
# ============================================

def remove_u2002(s):
    """Supprime le caractère \u2002 d'une chaîne."""
    return s.replace('\u2002', '')

# Usage
result = remove_u2002('0;"&gt;Unknown\u2002')
print(f"Résultat: {repr(result)}")

# ============================================
# Pour plus d'options, voir:
# - remove_unicode_spaces.py (script complet)
# - UNICODE_SPACES_GUIDE.md (documentation)
# - test_remove_unicode_spaces.py (tests)
# ============================================
