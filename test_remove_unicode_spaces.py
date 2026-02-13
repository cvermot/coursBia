#!/usr/bin/env python3
"""
Tests for remove_unicode_spaces.py

Run with: python3 test_remove_unicode_spaces.py
"""

import sys
from remove_unicode_spaces import (
    remove_en_space,
    remove_all_unicode_spaces,
    normalize_spaces
)


def test_remove_en_space():
    """Test removal of U+2002 (EN SPACE) character."""
    print("Testing remove_en_space()...")
    
    # Test case from problem statement
    assert remove_en_space('0;"&gt;Unknown\u2002') == '0;"&gt;Unknown'
    
    # Test with no EN SPACE
    assert remove_en_space('Hello World') == 'Hello World'
    
    # Test with multiple EN SPACES
    assert remove_en_space('Hello\u2002\u2002World') == 'HelloWorld'
    
    # Test with EN SPACE at different positions
    assert remove_en_space('\u2002Hello') == 'Hello'
    assert remove_en_space('Hello\u2002') == 'Hello'
    assert remove_en_space('\u2002Hello\u2002World\u2002') == 'HelloWorld'
    
    # Test empty string
    assert remove_en_space('') == ''
    
    # Test string with only EN SPACE
    assert remove_en_space('\u2002\u2002\u2002') == ''
    
    print("✓ All remove_en_space() tests passed")


def test_remove_all_unicode_spaces():
    """Test removal of all Unicode spacing characters."""
    print("Testing remove_all_unicode_spaces()...")
    
    # Test with EN SPACE
    assert remove_all_unicode_spaces('Hello\u2002World') == 'HelloWorld'
    
    # Test with EM SPACE
    assert remove_all_unicode_spaces('Hello\u2003World') == 'HelloWorld'
    
    # Test with THIN SPACE
    assert remove_all_unicode_spaces('Hello\u2009World') == 'HelloWorld'
    
    # Test with HAIR SPACE
    assert remove_all_unicode_spaces('Hello\u200AWorld') == 'HelloWorld'
    
    # Test with NARROW NO-BREAK SPACE
    assert remove_all_unicode_spaces('Hello\u202FWorld') == 'HelloWorld'
    
    # Test with mixed Unicode spaces
    assert remove_all_unicode_spaces('A\u2002B\u2003C\u2009D\u200AE\u202FF') == 'ABCDEF'
    
    # Test preserving regular spaces
    assert remove_all_unicode_spaces('Hello World') == 'Hello World'
    
    # Test empty string
    assert remove_all_unicode_spaces('') == ''
    
    print("✓ All remove_all_unicode_spaces() tests passed")


def test_normalize_spaces():
    """Test normalization of Unicode spacing characters."""
    print("Testing normalize_spaces()...")
    
    # Test with EN SPACE
    assert normalize_spaces('Hello\u2002World') == 'Hello World'
    
    # Test with multiple different Unicode spaces
    assert normalize_spaces('A\u2002B\u2003C\u2009D') == 'A B C D'
    
    # Test with custom replacement
    assert normalize_spaces('Hello\u2002World', replacement='_') == 'Hello_World'
    assert normalize_spaces('Hello\u2002World', replacement='') == 'HelloWorld'
    
    # Test preserving regular spaces
    assert normalize_spaces('Hello World') == 'Hello World'
    
    # Test empty string
    assert normalize_spaces('') == ''
    
    print("✓ All normalize_spaces() tests passed")


def test_edge_cases():
    """Test edge cases and special scenarios."""
    print("Testing edge cases...")
    
    # Test with special characters
    assert remove_en_space('café\u2002résumé') == 'caférésumé'
    
    # Test with numbers
    assert remove_en_space('123\u2002456') == '123456'
    
    # Test with HTML entities
    assert remove_en_space('&lt;tag&gt;\u2002') == '&lt;tag&gt;'
    
    # Test Unicode preservation
    assert remove_en_space('日本語\u2002テキスト') == '日本語テキスト'
    
    # Test with newlines and tabs (should be preserved)
    assert remove_en_space('Hello\u2002\n\tWorld') == 'Hello\n\tWorld'
    
    print("✓ All edge case tests passed")


def run_all_tests():
    """Run all test suites."""
    print("=" * 50)
    print("Running tests for remove_unicode_spaces.py")
    print("=" * 50 + "\n")
    
    try:
        test_remove_en_space()
        test_remove_all_unicode_spaces()
        test_normalize_spaces()
        test_edge_cases()
        
        print("\n" + "=" * 50)
        print("✓ ALL TESTS PASSED!")
        print("=" * 50)
        return 0
    except AssertionError as e:
        print("\n" + "=" * 50)
        print("✗ TEST FAILED!")
        print("=" * 50)
        print(f"Error: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(run_all_tests())
