(function () {
  const cfg = window.LT_CONFIG || {};
  const waBase = "https://wa.me/" + (cfg.whatsapp || "");

  // --- WhatsApp links -------------------------------------------------------
  const defaultMsg = "Hola, La Tribu. Me interesa saber más sobre la secundaria.";
  document.querySelectorAll("[data-wa]").forEach((a) => {
    const msg = a.getAttribute("data-wa") || defaultMsg;
    a.href = waBase + "?text=" + encodeURIComponent(msg);
    a.target = "_blank";
    a.rel = "noopener";
  });
  document.querySelectorAll("[data-wa-display]").forEach((el) => {
    el.textContent = cfg.whatsappDisplay || "";
  });

  // --- Social links ---------------------------------------------------------
  const social = cfg.social || {};
  document.querySelectorAll("[data-social]").forEach((a) => {
    const key = a.getAttribute("data-social");
    if (social[key]) {
      a.href = social[key];
      a.target = "_blank";
      a.rel = "noopener";
    } else {
      a.remove();
    }
  });
  document.querySelectorAll("[data-social-block]").forEach((block) => {
    if (!block.querySelector("a")) block.remove();
  });

  // --- Mobile menu ----------------------------------------------------------
  const menu = document.getElementById("menu");
  const toggle = document.querySelector(".nav__toggle");
  const close = document.querySelector(".menu__close");
  if (menu && toggle) {
    const open = (v) => {
      menu.dataset.open = v ? "true" : "false";
      toggle.setAttribute("aria-expanded", v ? "true" : "false");
      document.body.style.overflow = v ? "hidden" : "";
    };
    toggle.addEventListener("click", () => open(true));
    close && close.addEventListener("click", () => open(false));
    menu.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => open(false)));
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") open(false); });
  }

  // --- Current page in nav --------------------------------------------------
  const here = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav__links a, .menu a").forEach((a) => {
    const href = a.getAttribute("href");
    if (href === here) a.setAttribute("aria-current", "page");
  });

  // --- Reveal on scroll -----------------------------------------------------
  const reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add("is-visible"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px 0px 0px", threshold: 0.05 });
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("is-visible"));
  }

  // --- Lead form ------------------------------------------------------------
  const form = document.getElementById("lead-form");
  if (!form) return;
  const status = form.querySelector(".form__status");
  const submitBtn = form.querySelector('[type="submit"]');

  const setStatus = (state, html) => {
    status.dataset.state = state;
    status.innerHTML = html;
    status.scrollIntoView({ behavior: "smooth", block: "nearest" });
  };

  const buildSummary = (d) => [
    "Hola, La Tribu. Quiero información para inscribir a mi hijo/a.",
    "",
    "Nombre: " + d.nombre,
    "WhatsApp: " + d.whatsapp,
    d.email ? "Email: " + d.email : null,
    "Estudiante: " + d.estudiante + " (" + d.edad + " años)",
    "Grado de interés: " + d.grado,
    d.origen ? "Cómo nos conoció: " + d.origen : null,
    d.mensaje ? "Mensaje: " + d.mensaje : null
  ].filter(Boolean).join("\n");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    // honeypot
    if (form.querySelector('[name="botcheck"]').value) return;

    let valid = true;
    form.querySelectorAll("[required]").forEach((el) => {
      const field = el.closest(".field");
      const ok = el.checkValidity();
      field && field.classList.toggle("is-invalid", !ok);
      if (!ok) valid = false;
    });
    if (!valid) { setStatus("error", "Revisa los campos marcados, por favor."); return; }

    const fd = new FormData(form);
    const d = Object.fromEntries(fd.entries());
    const summary = buildSummary(d);

    if (!cfg.web3formsKey) {
      // Respaldo: abrir WhatsApp con el resumen de la solicitud.
      window.open(waBase + "?text=" + encodeURIComponent(summary), "_blank", "noopener");
      setStatus("success", "<strong>¡Gracias!</strong> Abrimos WhatsApp con tu solicitud lista para enviar. Si no se abrió, escríbenos al " + (cfg.whatsappDisplay || "") + ".");
      form.reset();
      return;
    }

    submitBtn.disabled = true;
    submitBtn.dataset.label = submitBtn.textContent;
    submitBtn.textContent = "Enviando…";
    try {
      const payload = {
        access_key: cfg.web3formsKey,
        subject: "Nuevo lead La Tribu — " + d.nombre + " (" + d.grado + ")",
        from_name: "Sitio La Tribu",
        replyto: d.email || undefined,
        ...d,
        resumen: summary
      };
      delete payload.botcheck;
      const res = await fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(payload)
      });
      const json = await res.json();
      if (json.success) {
        setStatus("success", "<strong>¡Recibimos tus datos!</strong> Te escribimos por WhatsApp en menos de 48 horas. Si prefieres, también puedes <a data-wa-inline href='#'>escribirnos ahora</a>.");
        const inline = status.querySelector("[data-wa-inline]");
        if (inline) { inline.href = waBase + "?text=" + encodeURIComponent(summary); inline.target = "_blank"; }
        form.reset();
      } else {
        throw new Error(json.message || "error");
      }
    } catch (err) {
      setStatus("error", "No pudimos enviar el formulario. Escríbenos por WhatsApp al " + (cfg.whatsappDisplay || "") + " y te atendemos.");
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = submitBtn.dataset.label;
    }
  });
})();
