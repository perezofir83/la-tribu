(function () {
  const cfg = window.LT_CONFIG || {};
  const waBase = "https://wa.me/" + (cfg.whatsapp || "");
  const LANG = document.body.dataset.lang || "es";
  const I18N = {
    es: { defaultMsg: "Hola, La Tribu. Me interesa saber más sobre la secundaria.",
          intro: "Hola, La Tribu. Quiero información para inscribir a mi hijo/a.",
          name: "Nombre", student: "Estudiante", years: "años", grade: "Grado de interés", source: "Cómo nos conoció", message: "Mensaje",
          invalid: "Revisa los campos marcados, por favor.",
          waOpened: "<strong>¡Gracias!</strong> Abrimos WhatsApp con tu solicitud lista para enviar. Si no se abrió, escríbenos al ",
          sending: "Enviando…", subject: "Nuevo lead La Tribu — ",
          ok: "<strong>¡Recibimos tus datos!</strong> Te escribimos por WhatsApp en menos de 48 horas. Si prefieres, también puedes <a data-wa-inline href='#'>escribirnos ahora</a>.",
          fail: "No pudimos enviar el formulario. Escríbenos por WhatsApp al " },
    en: { defaultMsg: "Hello, La Tribu. I'd like to know more about the school.",
          intro: "Hello, La Tribu. I'd like information to enroll my child.",
          name: "Name", student: "Student", years: "years old", grade: "Grade of interest", source: "How they found us", message: "Message",
          invalid: "Please check the highlighted fields.",
          waOpened: "<strong>Thank you!</strong> We opened WhatsApp with your request ready to send. If it didn't open, message us at ",
          sending: "Sending…", subject: "New lead La Tribu — ",
          ok: "<strong>We got your details!</strong> We'll message you on WhatsApp within 48 hours. You can also <a data-wa-inline href='#'>write to us now</a>.",
          fail: "We couldn't send the form. Message us on WhatsApp at " },
    fr: { defaultMsg: "Bonjour, La Tribu. Je souhaite en savoir plus sur l'école.",
          intro: "Bonjour, La Tribu. Je souhaite des informations pour inscrire mon enfant.",
          name: "Nom", student: "Élève", years: "ans", grade: "Niveau souhaité", source: "Comment il/elle nous a connus", message: "Message",
          invalid: "Merci de vérifier les champs signalés.",
          waOpened: "<strong>Merci !</strong> Nous avons ouvert WhatsApp avec votre demande prête à envoyer. Sinon, écrivez-nous au ",
          sending: "Envoi…", subject: "Nouveau lead La Tribu — ",
          ok: "<strong>Nous avons bien reçu vos coordonnées !</strong> Nous vous écrivons sur WhatsApp sous 48 heures. Vous pouvez aussi <a data-wa-inline href='#'>nous écrire maintenant</a>.",
          fail: "Impossible d'envoyer le formulaire. Écrivez-nous sur WhatsApp au " }
  };
  const T = I18N[LANG] || I18N.es;

  // --- WhatsApp links -------------------------------------------------------
  const defaultMsg = T.defaultMsg;
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
    T.intro,
    "",
    T.name + ": " + d.nombre,
    "WhatsApp: " + d.whatsapp,
    d.email ? "Email: " + d.email : null,
    T.student + ": " + d.estudiante + " (" + d.edad + " " + T.years + ")",
    T.grade + ": " + d.grado,
    d.origen ? T.source + ": " + d.origen : null,
    d.mensaje ? T.message + ": " + d.mensaje : null
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
    if (!valid) { setStatus("error", T.invalid); return; }

    const fd = new FormData(form);
    const d = Object.fromEntries(fd.entries());
    const summary = buildSummary(d);

    if (!cfg.web3formsKey) {
      // Respaldo: abrir WhatsApp con el resumen de la solicitud.
      window.open(waBase + "?text=" + encodeURIComponent(summary), "_blank", "noopener");
      setStatus("success", T.waOpened + (cfg.whatsappDisplay || "") + ".");
      form.reset();
      return;
    }

    submitBtn.disabled = true;
    submitBtn.dataset.label = submitBtn.textContent;
    submitBtn.textContent = T.sending;
    try {
      const payload = {
        access_key: cfg.web3formsKey,
        subject: T.subject + d.nombre + " (" + d.grado + ") [" + LANG + "]",
        from_name: "Sitio La Tribu",
        replyto: d.email || undefined,
        ...d,
        resumen: summary,
        idioma: LANG
      };
      delete payload.botcheck;
      const res = await fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(payload)
      });
      const json = await res.json();
      if (json.success) {
        setStatus("success", T.ok);
        const inline = status.querySelector("[data-wa-inline]");
        if (inline) { inline.href = waBase + "?text=" + encodeURIComponent(summary); inline.target = "_blank"; }
        form.reset();
      } else {
        throw new Error(json.message || "error");
      }
    } catch (err) {
      setStatus("error", T.fail + (cfg.whatsappDisplay || "") + ".");
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = submitBtn.dataset.label;
    }
  });
})();
