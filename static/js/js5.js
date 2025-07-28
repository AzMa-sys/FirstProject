// Open the Modal
function openModal() {
  document.getElementById("myModal").style.display = "block";
}

// Close the Modal
function closeModal() {
  document.getElementById("myModal").style.display = "none";
}

// Next/previous controls
function plusSlides(n, galleryIndex) {
  showSlides(slideIndex + n, galleryIndex);
}

// Thumbnail image controls
function currentSlide(n, galleryIndex) {
  showSlides(n, galleryIndex);
}

function showSlides(n, galleryIndex) {
  var i;
  // Получаем элементы только для текущей галереи
  var slides = document.querySelectorAll(`.gallery-container[data-index="${galleryIndex}"] .mySlides`);
  var dots = document.querySelectorAll(`.gallery-container[data-index="${galleryIndex}"] .demo`);
  var captionText = document.querySelector(`.gallery-container[data-index="${galleryIndex}"] .caption-container p`);

  // Корректируем индекс слайда
  if (n > slides.length) { n = 1 }
  if (n < 1) { n = slides.length }

  // Скрываем все слайды
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  // Убираем активный класс у всех миниатюр
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }

  // Показываем текущий слайд и активируем соответствующую миниатюру
  slides[n - 1].style.display = "block";
  dots[n - 1].className += "active";
  captionText.innerHTML = dots[n - 1].alt;

  // Обновляем глобальный индекс слайда
  slideIndex = n;
}