import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
css_files = [f for f in os.listdir('.') if f.endswith('.css')]

url_pattern = re.compile(r'(?:src=["\']?|url\([\'"]?)(https?://[^\'"\)]+)')
found_urls = set()

for f in html_files + css_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        urls = url_pattern.findall(content)
        for u in urls:
            found_urls.add((f, u))

for f, u in found_urls:
    print(f'{f}: {u}')
