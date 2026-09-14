// La Tribu — configuración del sitio.
// Edita este archivo y vuelve a publicar. No requiere build.
window.LT_CONFIG = {
  // WhatsApp de la escuela (solo dígitos, con lada de país).
  whatsapp: "5215642298959",
  whatsappDisplay: "+52 1 56 4229 8959",

  // Correo donde llegan los leads del formulario (el Gmail nuevo de La Tribu).
  leadEmail: "contact.escuelalatribu@gmail.com",

  // Copias: cada lead llega también a estos correos (CC vía Web3Forms).
  leadCc: ["Nellybordelais@icloud.com", "michal.weinberg@gmail.com"],

  // Proveedor de envío: "formsubmit" (gratis, sin key; https://formsubmit.co) o "web3forms" (requiere web3formsKey).
  // Con "formsubmit", el PRIMER envío manda un correo de activación a leadEmail: hay que hacer clic en "Activate".
  formProvider: "formsubmit",
  web3formsKey: "",

  // Redes sociales (deja vacío lo que no exista; el ícono se oculta solo).
  social: {
    instagram: "https://www.instagram.com/secundarialatribu",
    facebook: "",
    youtube: "",
    tiktok: ""
  }
};
