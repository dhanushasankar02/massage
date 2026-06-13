import os

directory = r"d:\message"

link_mapping = {
    'href="#home"': 'href="index.html"',
    'href="#home2"': 'href="home2.html"',
    'href="#about"': 'href="about.html"',
    'href="#services"': 'href="services.html"',
    'href="#therapists"': 'href="therapists.html"',
    'href="#corporate"': 'href="corporate events.html"',
    'href="#booknow"': 'href="book now.html"',
    'href="#giftcards"': 'href="gift card.html"',
    'href="#contact"': 'href="contact.html"',
    'href="#login"': 'href="login.html"',
}

js_active_snippet = """
    // --- Added for dynamic active state ---
    const currentPath = decodeURIComponent(window.location.pathname.split('/').pop()) || 'index.html';
    document.querySelectorAll('.nav-link, .dropdown-link').forEach(link => {
      const href = link.getAttribute('href');
      if (href && href !== '#' && href.includes(currentPath)) {
        link.classList.add('active');
        const parentLi = link.closest('li');
        if (parentLi) {
          const toggle = parentLi.querySelector('.dropdown-toggle');
          if (toggle) toggle.classList.add('active');
        }
      } else {
        link.classList.remove('active');
      }
    });
    // --- End dynamic active state ---
"""

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content
        for old_link, new_link in link_mapping.items():
            new_content = new_content.replace(old_link, new_link)

        import re
        new_content = re.sub(r'<script>\s*// --- Added for dynamic active state ---.*?// --- End dynamic active state ---\s*</script>', '', new_content, flags=re.DOTALL)
        if '</body>' in new_content:
            script_to_inject = f"<script>{js_active_snippet}</script>\n</body>"
            new_content = new_content.replace("</body>", script_to_inject)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Updated links and added active state script in all HTML files.")
