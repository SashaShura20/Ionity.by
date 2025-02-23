// Получаем элементы DOM
const modal = document.getElementById("myModal");
const openModalBtn = document.getElementById("openModalBtn");
const closeModalBtn = document.getElementById("closeModalBtn");

// Открываем модальное окно при клике на кнопку
openModalBtn.addEventListener("click", () => {
    modal.style.display = "block";
});

// Закрываем модальное окно при клике на крестик
closeModalBtn.addEventListener("click", () => {
    modal.style.display = "none";
});

// Закрываем модальное окно при клике вне его области
window.addEventListener("click", (event) => {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});

