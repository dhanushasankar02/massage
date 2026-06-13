import os
import re

html_files = [
    'about.html',
    'book now.html',
    'contact.html',
    'corporate events.html',
    'gift card.html',
    'home2.html',
    'services.html',
    'index.html'
]

hero_classes = [
    'hero', 'hero-booking', 'hero-contact', 'hero-corp', 'hero-gift', 'h2-hero', 'srv-hero'
]

for f in html_files:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content
    for hero_cls in hero_classes:
        # Regex to find the block defining the hero class
        # It looks for .classname { ... background: ... url('...') ... }
        # and replaces the url('...') with url('images/hero_bg.png')
        
        # We can just replace images/hero_bg_[a-zA-Z0-9\-]+\.jpg with images/hero_bg.png
        # but to be safe we only do this within the hero block.
        # Actually, simpler: in these files, any url('images/hero_bg_...jpg') that is the main hero background
        # wait, about.html has only one images/hero_bg_...jpg.
        pass

    # A simpler approach: just find `url('images/hero_bg_....jpg')` inside the <style> block and if it is in the hero class replace it.
    # Actually, why not just replace all url('images/hero_bg_....jpg') with url('images/hero_bg.png') if the user wants them all to be the SAME?
    # BUT wait, the therapists ones were also named `hero_bg_...jpg` by my script!
    # Therapists ones are in therapists.html, and they are used for `.member-image` inline styles: 
    # style="background-image: url('images/hero_bg_1544367567-0f2fcb009e0b.jpg');"
    # So if I replace ONLY in <style> block, I will hit the hero backgrounds, because the therapists ones are inline styles!
    
    # Wait, in contact.html there is another one: url('images/hero_bg_1524661135-423995f22d0b.jpg') inside `.contact-image-placeholder` or something?
    # Let me just use regex to target the specific hero classes.

    # Find .hero-class { ... url('...') ... }
    for cls in hero_classes:
        pattern = r'(\.' + cls + r'\s*\{[^}]*url\([\'"]?)(images/hero_bg_[^\'"\)]+)([\'"]?\)[^}]*\})'
        new_content = re.sub(pattern, r'\g<1>images/hero_bg.png\g<3>', new_content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)

print("Hero backgrounds updated to hero_bg.png")
