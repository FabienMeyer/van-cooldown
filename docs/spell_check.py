#!/usr/bin/env python3
"""
Simple spell checker for markdown files using pyenchant.
Replacement for pyspelling which requires aspell on Windows.
"""

import sys
import glob
import re
import enchant
from pathlib import Path

def extract_text_from_markdown(content):
    """Extract text from markdown, ignoring code blocks and other non-prose content."""
    # Remove code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    content = re.sub(r'`[^`]+`', '', content)
    
    # Remove markdown links but keep text
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
    
    # Remove markdown formatting
    content = re.sub(r'[*_#-]', ' ', content)
    content = re.sub(r'=+', '', content)
    
    # Remove URLs
    content = re.sub(r'https?://[^\s]+', '', content)
    
    return content

def load_custom_words():
    """Load custom words from the wordlist file."""
    custom_words = set()
    wordlist_path = Path('.spelling-wordlist.txt')
    if wordlist_path.exists():
        try:
            with open(wordlist_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        custom_words.add(line.lower())
        except Exception as e:
            print(f"Warning: Could not read custom wordlist: {e}")
    return custom_words

def check_file(file_path, dict_checker, custom_words=None):
    """Check spelling in a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"ERROR: Could not read {file_path}: {e}")
        return False
    
    text = extract_text_from_markdown(content)
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    errors = []
    for word in words:
        if len(word) > 2 and not dict_checker.check(word):
            # Check custom words
            if custom_words and word.lower() in custom_words:
                continue
            errors.append(word)
    
    if errors:
        print(f"Spelling errors in {file_path}:")
        unique_errors = sorted(set(errors))
        for error in unique_errors[:10]:  # Limit to first 10 errors
            suggestions = dict_checker.suggest(error)[:3]  # Top 3 suggestions
            print(f"  - {error} (suggestions: {', '.join(suggestions)})")
        if len(unique_errors) > 10:
            print(f"  ... and {len(unique_errors) - 10} more errors")
        return False
    
    return True

def main():
    """Main spell checking function."""
    if len(sys.argv) > 1:
        pattern = sys.argv[1]
    else:
        pattern = "src/**/*.md"
    
    print(f"Checking spelling in files matching: {pattern}")
    
    # Initialize spell checker
    try:
        # Try different dictionary backends
        dict_checker = None
        for lang_code in ["en_US", "en", "en_GB"]:
            try:
                dict_checker = enchant.Dict(lang_code)
                print(f"Using dictionary: {lang_code}")
                break
            except Exception as e:
                print(f"Failed to load {lang_code}: {e}")
                continue
        
        if dict_checker is None:
            # List available dictionaries for debugging
            print("Available dictionaries:")
            for provider in enchant.list_dicts():
                print(f"  - {provider[0]} ({provider[1].name})")
            raise Exception("No working dictionary found")
            
    except Exception as e:
        print(f"ERROR: Could not initialize spell checker: {e}")
        return 1
    
    # Load custom words
    custom_words = load_custom_words()
    print(f"Loaded {len(custom_words)} custom words")
    
    # Find files
    files = glob.glob(pattern, recursive=True)
    if not files:
        print(f"No files found matching pattern: {pattern}")
        return 1
    
    print(f"Found {len(files)} files to check")
    
    all_good = True
    for file_path in files:
        if not check_file(file_path, dict_checker, custom_words):
            all_good = False
    
    if all_good:
        print("✓ All files passed spell checking")
        return 0
    else:
        print("✗ Spelling errors found")
        return 1

if __name__ == "__main__":
    sys.exit(main())
