# Refugio Mi Mascota Bunny

Sitio web en español para el refugio de conejos en Tijuana, México.

## Páginas

| Archivo | Contenido |
|---------|-----------|
| `index.html` | Inicio, misión, conejos destacados |
| `adoptar.html` | Galería de adopción y requisitos |
| `hogar-temporal.html` | Hogar temporal, requisitos y formulario |
| `ayudar.html` | Donaciones, voluntariado y donaciones en especie |
| `contacto.html` | Redes sociales y mensaje de contacto (sin teléfono ni dirección) |
| `conejos/*.html` | Perfil individual de cada conejo en adopción |

## Vista local

Abre `index.html` en el navegador, o desde esta carpeta:

```bash
python3 -m http.server 8080
```

Luego visita http://localhost:8080

## Personalizar

1. **WhatsApp** — Edita el número en `js/main.js` (busca `526640000000`).
2. **Fotos** — Coloca las imágenes reales en `images/` con los mismos nombres que en el HTML (por ejemplo `copito.jpg`, `hero-home.jpg`). Si faltan, se muestra un placeholder rosa.
3. **PayPal / CLABE / QR** — Actualiza los datos reales en `ayudar.html`.
4. **Redes sociales** — Añade los enlaces en el pie de página de cada página.

## Estructura

```
mimascotabunny/
├── index.html
├── adoptar.html
├── hogar-temporal.html
├── ayudar.html
├── css/styles.css
├── js/main.js
└── images/          ← fotos del refugio
```

## Diseño

- Colores: maroon `#9b2d4e`, rosa `#fdeef4`, crema `#fdfbf9`, verde WhatsApp `#4caf50`
- Fuente: Montserrat (títulos en bold, texto en regular)
- Responsive: barra inferior en móvil, menú superior en escritorio
