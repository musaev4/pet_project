document.getElementById('burgerMenu').addEventListener('click', function () {
    var x = document.getElementById("myNav");
    if (x.className === "nav-bar") {
        x.className += " responsive";
    } else {
        x.className = "nav-bar";
    }
});

// Закрытие бургер-меню при выборе пункта меню на мобильных устройствах
var navLinks = document.querySelectorAll('.nav-bar a');
navLinks.forEach(function (navLink) {
    navLink.addEventListener('click', function () {
        var navBar = document.getElementById("myNav");
        if (navBar.className.includes("responsive")) {
            navBar.className = "nav-bar";
        }
    });
});