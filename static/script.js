const menuButton = document.querySelector(".menu-toggle");
const nav = document.querySelector(".main-nav");

if (menuButton && nav) {
  menuButton.addEventListener("click", () => {
    const opened = nav.classList.toggle("open");
    menuButton.setAttribute("aria-expanded", String(opened));
  });

  nav.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => {
      nav.classList.remove("open");
      menuButton.setAttribute("aria-expanded", "false");
    });
  });
}

const searchInput = document.querySelector("#playerSearch");
if (searchInput) {
  searchInput.addEventListener("keydown", event => {
    if (event.key === "Escape") searchInput.value = "";
  });
}
