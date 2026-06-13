import os
import re

directory = r"d:\message"
index_file = os.path.join(directory, "index.html")

# Read index.html
with open(index_file, "r", encoding="utf-8") as f:
    index_content = f.read()

# Extract navbar from index.html
navbar_match = re.search(r'(<header class="navbar" id="mainNavbar">.*?</header>)', index_content, re.DOTALL)
if not navbar_match:
    print("Navbar not found in index.html")
    exit(1)

new_navbar = navbar_match.group(1)
print(f"Extracted navbar of length {len(new_navbar)}")

# Iterate over all html files
for filename in os.listdir(directory):
    if filename.endswith(".html") and filename not in ["index.html", "navbar.html"]:
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace existing navbar
        # Assuming the navbar is also between <header class="navbar" id="mainNavbar"> and </header>
        # or just <header ...> ... </header>
        
        # Let's search for <header class="navbar" id="mainNavbar"> or similar.
        if '<header class="navbar"' in content:
            updated_content = re.sub(r'<header class="navbar"[^>]*>.*?</header>', new_navbar, content, flags=re.DOTALL)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Updated {filename}")
        else:
            print(f"No navbar found in {filename}")

print("Done.")
