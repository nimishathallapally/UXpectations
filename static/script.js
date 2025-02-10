document.addEventListener("wheel", function(event) {
    window.scrollBy(0, -event.deltaY*3);  // Reverse the direction
    event.preventDefault();
}, { passive: false });

function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

// Save dark mode preference
if (localStorage.getItem("dark-mode") === "enabled") {
    document.body.classList.add("dark-mode");
}

document.querySelector(".toggle-mode").addEventListener("click", function () {
    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("dark-mode", "enabled");
    } else {
        localStorage.setItem("dark-mode", "disabled");
    }
});