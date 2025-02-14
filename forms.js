let dataArray =[];

const form = document.getElementById(myForm);
const dataList = document.getElementById(DataList);

form.addEventListener('submit', function (event) {
    event.preventDefault();
})


const formData = {
    name: form.name.value,
    email: form.email.value,
    password: form.email.value
};



dataArray.push(formData);


form.reset();


 function updateDataList() {
     DataList.innerHTML = '';


     dataArray.forEach((item, index) => {
         const listItem = document.createElement('li');
         listItem.textContent = `Запись ${index + 1} : Имя - ${item.name}, Email - ${item.email}, Пароль - ${item.password}`
     });

 }