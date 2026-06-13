import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Replace FontAwesome CDN with local path
    content = content.replace(
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css', 
        'fontawesome/fontawesome-free-6.0.0-web/css/all.min.css'
    )
    
    # Remove Google Fonts
    content = re.sub(r'<link[^>]*href="https://fonts\.googleapis\.com[^>]*>\s*', '', content)
    
    # Fix therapists hero
    content = re.sub(
        r'background:\s*linear-gradient\(135deg,\s*var\(--bg-surface\)\s*0%,\s*var\(--accent-light\)\s*100%\);', 
        r"background: url('images/hero_bg.png') center/cover no-repeat;", 
        content
    )
    
    # Ensure any remaining hero backgrounds are using the same image
    # Note: the previous script replaced most of them, so we just check for missed ones if any
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
print("Fixed hero backgrounds and offline mode paths.")
