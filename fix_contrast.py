import os
import re
import glob

def process_css_block(match):
    block = match.group(0)
    # Check if the block has an accent background
    if re.search(r'background:\s*(?:var\(--accent\)|linear-gradient[^;]+var\(--accent\))', block) or \
       re.search(r'background-color:\s*var\(--accent\)', block):
        # Only replace color: #fff; if it's in the same block
        block = re.sub(r'color:\s*#fff(?:fff)?\s*;', 'color: var(--accent-text);', block)
    return block

def main():
    files = glob.glob('*.html')
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Add --accent-text to :root
        if '--accent-text:' not in content:
            content = re.sub(
                r'(:root\s*\{[^}]+)(--navbar-bg)',
                r'\1--accent-text: #ffffff;\n      \2',
                content,
                count=1
            )

        # 2. Add --accent-text to body.dark-mode
        # Use regex to find body.dark-mode block and insert --accent-text if not present
        if 'body.dark-mode' in content:
            dark_mode_match = re.search(r'body\.dark-mode\s*\{([^}]+)\}', content)
            if dark_mode_match and '--accent-text:' not in dark_mode_match.group(1):
                content = re.sub(
                    r'(body\.dark-mode\s*\{[^}]+)(--navbar-bg)',
                    r'\1--accent-text: #121212;\n      \2',
                    content,
                    count=1
                )

        # 3. Replace color: #fff; with color: var(--accent-text); in blocks with var(--accent) background
        content = re.sub(r'[^\{\}]+\{[^}]+\}', process_css_block, content)
        
        classes_to_fix = [
            r'(\.btn-primary\s*\{[^\}]+)color:\s*#fff(?:fff)?\s*;',
            r'(\.logo-mark\s*\{[^\}]+)color:\s*#fff(?:fff)?\s*;',
            r'(\.btn-corp-gift\s*\{[^\}]+)color:\s*#fff(?:fff)?\s*;',
            r'(\.gift-btn\s*\{[^\}]+)color:\s*#fff(?:fff)?\s*;',
            r'(\.btn-login\s*\{[^\}]+)color:\s*#fff(?:fff)?\s*;',
            r'(\.btn-register\s*\{[^\}]+)color:\s*#fff(?:fff)?\s*;',
            r'(\.srv-btn\s*\{[^\}]+)color:\s*#fff(?:fff)?\s*;',
            r'(\.srv-price-btn\s*\{[^\}]+)color:\s*#fff(?:fff)?\s*;',
            r'(\.book-btn\s*\{[^\}]+)color:\s*#fff(?:fff)?\s*;',
            r'(\.join-btn\s*\{[^\}]+)color:\s*#fff(?:fff)?\s*;',
            r'(\.checkout-btn\s*\{[^\}]+)color:\s*#fff(?:fff)?\s*;',
            r'(\.social-links-footer a:hover\s*\{[^\}]+)color:\s*white\s*;',
            r'(\.btn-outline:hover\s*\{[^\}]+)color:\s*white\s*;',
        ]
        
        for c_regex in classes_to_fix:
            content = re.sub(c_regex, r'\1color: var(--accent-text);', content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'Processed {file}')

if __name__ == "__main__":
    main()
