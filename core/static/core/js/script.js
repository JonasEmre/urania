function showMenu() {
  const hamburgerMenu = document.getElementById("hamburgerMenu");
  const hamburgerLine = document.getElementById("hamburgerLine");

  if (
    hamburgerMenu.style.display == "none" ||
    hamburgerMenu.style.display == ""
  ) {
    hamburgerMenu.style.display = "block";
    hamburgerLine.className = "hamburger__line rotate-hamburger";
  } else {
    hamburgerMenu.style.display = "none";
    hamburgerLine.className = "hamburger__line";
  }
}

const messageContainer = document.getElementById("messageContainer");

setTimeout(function () {
  if (messageContainer) {
    messageContainer.style.display = "none";
  }
}, 7000); // Removes flash messages after spesific time
