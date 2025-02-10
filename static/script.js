document.addEventListener("wheel", function(event) {
    window.scrollBy(0, -event.deltaY);  // Reverse the direction
    event.preventDefault();
}, { passive: false });
