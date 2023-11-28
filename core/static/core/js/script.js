function showMenu() {
    const hamburgerMenu = document.getElementById("hamburger-menu");
    if (hamburgerMenu.style.display == "none" || hamburgerMenu.style.display == "") {
        hamburgerMenu.style.display = "block";
    } else {
        hamburgerMenu.style.display = "none";
    }
}