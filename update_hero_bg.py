import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Replace the old image reference with the new one
    new_content = content.replace("images/hero_bg.png", "images/new_hero_bg.png")
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
print("Updated all hero background images to new_hero_bg.png.")
