const burger = document.getElementById('burger');
const navList = document.getElementById('navList');

burger.addEventListener('click', () => {
    navList.classList.toggle('show'); // Переключаем класс "show" у списка навигации
    burger.classList.toggle('active'); // Добавляем активный класс для анимации кнопки-бургера
});
