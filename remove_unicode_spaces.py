#!/usr/bin/env python3
"""
Utility script to remove Unicode spacing characters from strings.

This script provides functions to remove the U+2002 (EN SPACE) character
and other Unicode spacing characters from strings.

Example usage:
    python3 remove_unicode_spaces.py
"""

import re

# Module-level constant for Unicode spacing characters
UNICODE_SPACES = [
    '\u2002',  # EN SPACE
    '\u2003',  # EM SPACE
    '\u2009',  # THIN SPACE
    '\u200A',  # HAIR SPACE
    '\u202F',  # NARROW NO-BREAK SPACE
]

# Compiled regex pattern for efficient replacement
_UNICODE_SPACES_PATTERN = re.compile('|'.join(re.escape(s) for s in UNICODE_SPACES))


def remove_en_space(text):
    """
    Remove U+2002 (EN SPACE) character from a string.
    
    Args:
        text (str): Input string that may contain EN SPACE characters
        
    Returns:
        str: String with EN SPACE characters removed
        
    Example:
        >>> s = '0;"&gt;Unknown\u2002'
        >>> remove_en_space(s)
        '0;"&gt;Unknown'
    """
    return text.replace('\u2002', '')


def remove_all_unicode_spaces(text):
    """
    Remove all Unicode spacing characters from a string.
    
    This includes:
    - U+2002 (EN SPACE)
    - U+2003 (EM SPACE)
    - U+2009 (THIN SPACE)
    - U+200A (HAIR SPACE)
    - U+202F (NARROW NO-BREAK SPACE)
    
    Args:
        text (str): Input string that may contain Unicode spacing characters
        
    Returns:
        str: String with Unicode spacing characters removed
    """
    return _UNICODE_SPACES_PATTERN.sub('', text)


def normalize_spaces(text, replacement=' '):
    """
    Replace all Unicode spacing characters with a standard space.
    
    Args:
        text (str): Input string that may contain Unicode spacing characters
        replacement (str): Character to replace Unicode spaces with (default: ' ')
        
    Returns:
        str: String with Unicode spacing characters replaced
    """
    return _UNICODE_SPACES_PATTERN.sub(replacement, text)


if __name__ == '__main__':
    # Demonstration examples
    print("=== Démonstration de suppression du caractère \\u2002 ===\n")
    
    # Example from the problem statement
    example_string = '0;"&gt;Unknown\u2002'
    print(f"Chaîne originale: {repr(example_string)}")
    print(f"Chaîne nettoyée:  {repr(remove_en_space(example_string))}\n")
    
    # Additional examples
    test_cases = [
        '0;"&gt;Unknown\u2002',
        'Texte avec\u2002espace EN',
        'Multiple\u2002\u2002espaces',
        'Mixed\u2002spaces\u2003and\u2009tabs',
    ]
    
    print("=== Autres exemples ===\n")
    for test in test_cases:
        cleaned = remove_en_space(test)
        all_cleaned = remove_all_unicode_spaces(test)
        normalized = normalize_spaces(test)
        
        print(f"Original:        {repr(test)}")
        print(f"Sans \\u2002:     {repr(cleaned)}")
        print(f"Sans tous:       {repr(all_cleaned)}")
        print(f"Normalisé:       {repr(normalized)}")
        print()
