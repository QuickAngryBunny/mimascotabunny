#!/usr/bin/env python3
"""Generate rabbit profile pages."""
from pathlib import Path

FORM = "https://docs.google.com/forms/d/1a9aEypXsQRid9wPjRVSvWVJv3CboCY_4H8e8zj7e1ss/"

GENERIC_DESCRIPTION = (
    "Es un conejo rescatado en Tijuana que busca un hogar lleno de amor y cuidado responsable. "
    "Con paciencia y el ambiente adecuado, se adapta muy bien a su nueva familia."
)

REQUIREMENTS = """
<ol class="adoption-requirements-list">
  <li>Estrictamente adopción de conejo para mascota: no venta, no reproducción, no comida.</li>
  <li>No como regalo ni mascota de niños.</li>
  <li>No tenerlos en jaula.</li>
  <li>Alimentación correcta a base de heno y pellets con alto contenido de fibra, y agua potable.</li>
  <li>Visita anual con veterinario de exóticos para consulta, vacunas y en caso de enfermedad.</li>
  <li>Seguimiento con fotografías cada semana el primer mes y después cada mes por un año.</li>
  <li>En caso de no poder cuidarlo, deberá entregarse al refugio; no regalarlo ni darlo en adopción por cuenta propia.</li>
  <li>Donación de costal de conejina (25 kg) o equivalente monetario (aprox. $350 MXN) para nuestros rescatados.</li>
</ol>
<p class="adoption-followup">Si cumples con los requisitos, llena la solicitud de adopción. Una vez enviada, escríbenos por redes sociales para darte seguimiento. Se hará entrevista por este medio y se solicitará INE, comprobante de domicilio y la firma del contrato de adopción.</p>
"""

RABBITS = [
    {"slug": "bobby", "name": "Bobby", "image": "bobby.jpg", "sex": "Macho"},
    {"slug": "choco", "name": "Choco", "image": "choco.jpg", "sex": "Macho"},
    {"slug": "dalmita", "name": "Dalmita", "image": "dalmita.jpg", "sex": "Hembra"},
    {"slug": "galan", "name": "Galán", "image": "galan.jpg", "sex": "Macho"},
    {"slug": "hershey", "name": "Hershey", "image": "hershey.jpg", "sex": "Hembra"},
    {"slug": "jazmin", "name": "Jazmín", "image": "jazmin.jpg", "sex": "Hembra"},
]

TEMPLATE = """<!DOCTYPE html>
<html lang="es-MX">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Adopta a {name} — Refugio Mi Mascota Bunny, Tijuana.">
  <title>{name} | Adoptar | Refugio Mi Mascota Bunny</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <button class="nav-toggle" type="button" aria-label="Abrir menú" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
      <a href="../index.html" class="logo-link">
        <img src="../images/logo-rmmb.png" alt="Refugio Mi Mascota Bunny" class="logo-img">
      </a>
      <nav class="nav-desktop" aria-label="Principal">
        <a href="../index.html">Inicio</a>
        <a href="../adoptar.html" class="active">Adoptar</a>
        <a href="../hogar-temporal.html">Hogar Temporal</a>
        <a href="../ayudar.html">Ayudar</a>
        <a href="../contacto.html">Contacto</a>
      </nav>
      <div class="header-social header-social-mobile" aria-label="Redes sociales">{social}</div>
      <div class="header-social header-social-desktop" aria-label="Redes sociales">{social}</div>
      <a href="../adoptar.html" class="btn btn-primary btn-sm header-cta">Adoptar</a>
    </div>
    <nav class="nav-mobile-panel" aria-label="Menú móvil">
      <a href="../index.html">Inicio</a>
      <a href="../adoptar.html">Adoptar</a>
      <a href="../hogar-temporal.html">Hogar Temporal</a>
      <a href="../ayudar.html">Ayudar</a>
      <a href="../contacto.html">Contacto</a>
      <div class="header-social">{social}</div>
    </nav>
  </header>

  <main>
    <section class="section rabbit-profile">
      <div class="container rabbit-profile-inner">
        <a href="../adoptar.html" class="back-link">← Volver a adoptar</a>
        <div class="rabbit-profile-grid">
          <div class="rabbit-profile-photo">
            <span class="tag tag-green">Listo para adopción</span>
            <img src="../images/{image}" alt="{name}">
          </div>
          <div class="rabbit-profile-info">
            <h1>{name}</h1>
            <ul class="rabbit-facts">
              <li><strong>Edad:</strong> 1 año</li>
              <li><strong>Sexo:</strong> {sex}</li>
              <li><strong>Esterilización:</strong> {steril}</li>
            </ul>
            <h2>Descripción</h2>
            <p>{description}</p>
          </div>
        </div>

        <div class="requirements-box adoption-requirements-block">
          <h2>Requisitos de adopción</h2>
          {requirements}
          <a href="{form}" class="btn btn-primary btn-adoption-form" target="_blank" rel="noopener noreferrer">Llenar solicitud</a>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container footer-simple">
      <a href="../index.html" class="logo-link footer-logo"><img src="../images/logo-rmmb.png" alt="Refugio Mi Mascota Bunny" class="logo-img logo-img-footer"></a>
      <nav class="footer-links">
        <a href="../contacto.html">Contacto</a>
        <a href="../ayudar.html">Donaciones</a>
      </nav>
      <p class="footer-copy">© 2024 Refugio Mi Mascota Bunny — Tijuana, México</p>
    </div>
  </footer>

  <nav class="bottom-nav" aria-label="Navegación inferior">
    <a href="../index.html"><span class="nav-icon-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></span>Inicio</a>
    <a href="../adoptar.html" class="active"><span class="nav-icon-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="4"/><path d="M6 20c0-4 2.7-6 6-6s6 2 6 6"/></svg></span>Adoptar</a>
    <a href="../hogar-temporal.html"><span class="nav-icon-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></span>Hogar</a>
    <a href="../ayudar.html"><span class="nav-icon-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></span>Ayudar</a>
  </nav>
  <script src="../js/site-config.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

SOCIAL = """
<a href="https://www.facebook.com/mimascotabunny" class="social-icon-btn" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
<a href="https://www.instagram.com/mimascotabunny/" class="social-icon-btn" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
<a href="https://www.tiktok.com/@mimascotabunny" class="social-icon-btn" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1-.1z"/></svg></a>
"""

out = Path(__file__).resolve().parent.parent / "conejos"
out.mkdir(exist_ok=True)

# Remove old profile pages
for old in out.glob("*.html"):
    old.unlink()

for r in RABBITS:
    steril = "Esterilizada" if r["sex"] == "Hembra" else "Esterilizado"
    html = TEMPLATE.format(
        **r,
        social=SOCIAL,
        requirements=REQUIREMENTS,
        form=FORM,
        description=GENERIC_DESCRIPTION,
        steril=steril,
    )
    (out / f"{r['slug']}.html").write_text(html, encoding="utf-8")
    print("wrote", r["slug"])
