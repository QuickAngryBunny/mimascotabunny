#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOCIAL = (ROOT / "partials/social-icons.html").read_text().strip()
FORM = "https://docs.google.com/forms/d/1a9aEypXsQRid9wPjRVSvWVJv3CboCY_4H8e8zj7e1ss/"

FONT_OLD = "family=DM+Sans"
FONT_NEW = "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap"

def patch_file(path: Path, active: str):
    text = path.read_text(encoding="utf-8")
    # Font
    import re
    text = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?[^"]+" rel="stylesheet">',
        f'<link href="{FONT_NEW}" rel="stylesheet">',
        text,
        count=1,
    )
    # Remove duplicate logos -> single logo
    text = re.sub(
        r'<a href="index\.html" class="logo logo-mobile">[^<]+</a>\s*'
        r'<a href="index\.html" class="logo logo-desktop">[^<]+</a>',
        '<a href="index.html" class="logo-link">\n        <img src="images/logo-rmmb.png" alt="Refugio Mi Mascota Bunny" class="logo-img">\n      </a>',
        text,
    )
    # Add Contacto to nav if missing
    if "contacto.html" not in text:
        text = text.replace(
            '<a href="ayudar.html">Ayudar</a>\n      </nav>',
            '<a href="ayudar.html">Ayudar</a>\n        <a href="contacto.html">Contacto</a>\n      </nav>',
        )
        text = text.replace(
            '<a href="ayudar.html">Ayudar</a>\n      <div class="header-social">',
            '<a href="ayudar.html">Ayudar</a>\n      <a href="contacto.html">Contacto</a>\n      <div class="header-social">',
        )
    # Social icons with TikTok
    for block in ["header-social-mobile", "header-social-desktop"]:
        pattern = rf'(<div class="header-social {block}"[^>]*>)(.*?)(</div>)'
        text = re.sub(pattern, rf"\1\n        {SOCIAL}\n      \3", text, flags=re.DOTALL)
    # Mobile panel social
    text = re.sub(
        r'(<nav class="nav-mobile-panel"[^>]*>.*?<div class="header-social">)(.*?)(</div>)',
        rf"\1\n        {SOCIAL}\n      \3",
        text,
        flags=re.DOTALL,
        count=1,
    )
    # Active nav
    text = re.sub(r'class="active"', "", text)
    if active == "adoptar":
        text = text.replace('<a href="adoptar.html">Adoptar</a>', '<a href="adoptar.html" class="active">Adoptar</a>', 1)
    elif active:
        text = text.replace(f'<a href="{active}.html">', f'<a href="{active}.html" class="active">', 1)
    # Footer contact
    text = text.replace('<a href="#" data-whatsapp>Contacto</a>', '<a href="contacto.html">Contacto</a>')
    # site-config script
    if "site-config.js" not in text:
        text = text.replace(
            '<script src="js/main.js"></script>',
            '<script src="js/site-config.js"></script>\n  <script src="js/main.js"></script>',
        )
    # Adoption form buttons
    text = text.replace('data-whatsapp>Llenar Solicitud', f'href="{FORM}" target="_blank" rel="noopener noreferrer" class="btn-adoption-form">Llenar solicitud')
    text = text.replace('class="btn btn-outline btn-block" data-whatsapp>Llenar Solicitud', f'class="btn btn-outline btn-block btn-adoption-form" href="{FORM}" target="_blank" rel="noopener noreferrer">Llenar solicitud')
    path.write_text(text, encoding="utf-8")
    print("patched", path.name)

for name, active in [
    ("index.html", "index"),
    ("adoptar.html", "adoptar"),
    ("hogar-temporal.html", "hogar-temporal"),
    ("ayudar.html", "ayudar"),
]:
    patch_file(ROOT / name, active)
