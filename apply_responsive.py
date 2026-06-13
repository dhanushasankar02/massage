import os
import glob

def apply_css():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already added
        if 'responsive.css' in content:
            print(f"Skipping {file}, already has responsive.css")
            continue
            
        # Add stylesheet right before </head>
        if '</head>' in content:
            new_content = content.replace('</head>', '  <link rel="stylesheet" href="responsive.css">\n</head>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
        else:
            print(f"Could not find </head> in {file}")

if __name__ == '__main__':
    apply_css()
