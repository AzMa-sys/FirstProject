// Простой скрипт для анимации
document.addEventListener("DOMContentLoaded", function() {
    const products = document.querySelectorAll(".product");

    products.forEach(product => {
        product.addEventListener("mouseenter", function() {
            product.style.transform = "scale(1.05)";
            product.style.transition = "transform 0.3s ease";
        });

        product.addEventListener("mouseleave", function() {
            product.style.transform = "scale(1)";
        });
    });
});
