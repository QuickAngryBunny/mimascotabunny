(function () {
  const config = window.RMMB || {};
  const ADOPTION_FORM =
    config.adoptionFormUrl ||
    "https://docs.google.com/forms/d/1a9aEypXsQRid9wPjRVSvWVJv3CboCY_4H8e8zj7e1ss/";

  document.querySelectorAll(".btn-adoption-form").forEach((el) => {
    el.setAttribute("href", ADOPTION_FORM);
    el.setAttribute("target", "_blank");
    el.setAttribute("rel", "noopener noreferrer");
  });

  const WHATSAPP_URL =
    "https://wa.me/526640000000?text=" +
    encodeURIComponent(
      "Hola, me interesa apoyar a Refugio Mi Mascota Bunny en Tijuana."
    );

  document.querySelectorAll("[data-whatsapp]").forEach((el) => {
    el.setAttribute("href", WHATSAPP_URL);
    el.setAttribute("target", "_blank");
    el.setAttribute("rel", "noopener noreferrer");
  });

  const navToggle = document.querySelector(".nav-toggle");
  const navPanel = document.querySelector(".nav-mobile-panel");
  if (navToggle && navPanel) {
    navToggle.addEventListener("click", () => {
      const open = navPanel.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", open);
    });
    navPanel.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        navPanel.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  document.querySelectorAll(".accordion-trigger").forEach((btn) => {
    btn.addEventListener("click", () => {
      const item = btn.closest(".accordion-item");
      const open = item.classList.toggle("open");
      btn.setAttribute("aria-expanded", open);
    });
  });

  const copyBtn = document.querySelector("[data-copy-clabe]");
  if (copyBtn) {
    const clabe = copyBtn.getAttribute("data-clabe") || "012 345 6789 0123 4567";
    copyBtn.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(clabe.replace(/\s/g, ""));
        const prev = copyBtn.textContent;
        copyBtn.textContent = "¡Copiado!";
        setTimeout(() => {
          copyBtn.textContent = prev;
        }, 2000);
      } catch {
        alert("CLABE: " + clabe);
      }
    });
  }

  document.querySelectorAll("form[data-form]").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const name = form.querySelector("[name=nombre]")?.value || "";
      const msg =
        "Hola, envío mi solicitud desde el sitio web." +
        (name ? " Nombre: " + name : "");
      window.open(
        "https://wa.me/526640000000?text=" + encodeURIComponent(msg),
        "_blank"
      );
    });
  });
})();
