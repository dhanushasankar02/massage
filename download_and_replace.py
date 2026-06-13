import os
import re
import urllib.request
import hashlib

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

url_pattern = re.compile(r'(https://images\.unsplash\.com/[^\'"\)\s]+)')

url_to_filename = {}
counter = 1

os.makedirs('images', exist_ok=True)

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    urls = url_pattern.findall(content)
    if not urls:
        continue
        
    new_content = content
    for u in urls:
        if u not in url_to_filename:
            # Check if it is a photo ID to name it nicely
            match = re.search(r'photo-([a-zA-Z0-9\-]+)', u)
            if match:
                filename = f"hero_bg_{match.group(1)}.jpg"
            else:
                filename = f"unsplash_{counter}.jpg"
                counter += 1
                
            filepath = os.path.join('images', filename)
            print(f"Downloading {u} to {filepath}...")
            
            # Add user agent to prevent 403 Forbidden
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
            try:
                with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                    out_file.write(response.read())
            except Exception as e:
                print(f"Failed to download {u}: {e}")
                continue
                
            url_to_filename[u] = f"images/{filename}"
            
        new_content = new_content.replace(u, url_to_filename[u])
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)

print("Done replacing images.")
