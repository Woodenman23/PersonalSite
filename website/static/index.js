function changeNavbarColor() {
    const navbar = document.querySelector(".navbar");
    const hue = Math.floor(Math.random() * 360);

    let backgroundColor = `hsl(${hue}, 70%, 60%)`;
    let textColor;

    if (hue >= 45 && hue <= 165) {
        textColor = "#333333";
    }
    else {
        textColor = "white";
    }

    navbar.style.transition = "background-color 1.5s ease-in-out";
    navbar.style.backgroundColor = backgroundColor;


    document.querySelectorAll(".navbar .nav-link").forEach(link => {
        link.style.transition = "color 1.5s ease-in-out";
        link.style.color = textColor;
    });

    const togglerIcon = document.querySelector(".navbar-toggler-icon");
    if (togglerIcon) {
        togglerIcon.style.filter = textColor === "white" ? "invert(1)" : "invert(0)";
    }


}


setInterval(changeNavbarColor, 3000);