// Массив для хранения данных
let dataArray = [];

// Получаем форму и список для отображения данных
const form = document.getElementById('myForm');
const dataList = document.getElementById('dataList');

// Обработчик отправки формы
form.addEventListener('submit', function (event) {
    event.preventDefault(); // Отменяем стандартное поведение формы

    // Создаем объект с данными из формы
    const formData = {
        name: form.name.value,
        email: form.email.value,
        password: form.password.value, // Пароль сохраняется как обычный текст
    };

    // Добавляем объект в массив
    dataArray.push(formData);

    // Очищаем форму
    form.reset();

    // Обновляем отображение данных
    updateDataList();
});

// Функция для обновления списка данных
function updateDataList() {
    // Очищаем список
    dataList.innerHTML = '';

    // Добавляем каждый элемент массива в список
    dataArray.forEach((item, index) => {
        const listItem = document.createElement('li');
        listItem.textContent = `Запись ${index + 1}: Имя - ${item.name}, Email - ${item.email}, Пароль - ${item.password}`;
        dataList.appendChild(listItem);
    });
}