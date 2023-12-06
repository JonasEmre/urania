function showMenu() {
  const hamburgerMenu = document.getElementById("hamburger-menu");
  const hamburgerLine = document.getElementById("hamburger-line");

  if (
    hamburgerMenu.style.display == "none" ||
    hamburgerMenu.style.display == ""
  ) {
    hamburgerMenu.style.display = "block";
    hamburgerLine.className = "hamburger__line rotate-hamburger"
  } else {
    hamburgerMenu.style.display = "none";
    hamburgerLine.className = "hamburger__line"
  }
}
