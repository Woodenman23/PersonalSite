function changeNavbarColor() {
    const navbar = document.querySelector(".navbar");
    const hue = Math.floor(Math.random() * 360);

    let backgroundColor = `hsl(${hue}, 80%, 80%)`;
    let textColor = `hsl(${(hue + 180) % 360}, 80%, 40%)`;

    navbar.style.transition = "background-color 1.5s ease-in-out";
    navbar.style.backgroundColor = backgroundColor;


    document.querySelectorAll(".navbar .nav-link").forEach(link => {
        link.style.transition = "color 1.5s ease-in-out";
        link.style.color = textColor;
    });
}

setInterval(changeNavbarColor, 3000);