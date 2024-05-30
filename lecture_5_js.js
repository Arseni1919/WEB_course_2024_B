// console.log('wwwww');


// const x = 5;
//
// const y = '5';

// console.log(`x == y is ${x == y}`);
// console.log(`x == y is ${x === y}`);

// const x = 5;
// const y = 10;

// if (x > 2 || y > 10) {
// if (x > 2 && y > 1) {
//     console.log('Inside!');
// } else {
//     console.log('Outside!');
// }

// const x = 11;
// const color = x > 10 ? 'red': 'blue';
// console.log(color);

// const color = 'red';
//
// switch (color) {
//     case 'red':
//         console.log('color is red');
//         break;
//     case 'blue':
//         console.log('color is blue');
//         break;
//     case 'green':
//         console.log('color is green');
//         break;
//     default:
//         console.log('gray');
//         break;
// }


// function addNums1(num1, num2) {
//     console.log(num1 + num2);
// }
//
// function addNums2(num1, num2 = 2) {
//     return num1 + num2;
// }
//
// addNums1(10, 20)
// console.log(addNums2(10, 20));
// console.log(addNums2(100));

// const addNums1 = (num1, num2) => {
//     return num1 + num2
// }
//
// const addNums2 = (num1, num2) => num1 + num2
//
//
// const addOne = num1 => num1 + 1

const todos = [
    {
        id: 1,
        text: 'do homework',
        isComplete: true,
    },
        {
        id: 2,
        text: 'do dishes',
        isComplete: true,
    },
        {
        id: 3,
        text: 'meeting',
        isComplete: false,
    },
];

// const printName = todo => console.log(todo.text)
// todos.forEach(printName);


// todos.forEach(todo => console.log(todo.text));

// function Person(firstName, lastName, dob) {
//     this.firstName = firstName;
//     this.lastName = lastName;
//     this.dob = new Date(dob);
//     this.getBirthYear = () => this.dob.getFullYear()
//     this.getFullName = () => `My name is: ${this.firstName} ${this.lastName}.`
// }
//
// Person.prototype.getBirthYear2 = () => {
//     return `My year is ${this.dob}.`;
// }

// const person1 = new Person('Moti', 'Katz', '4-3-1980');
// const person2 = new Person('Rina', 'Katz', '4-3-1988');

// console.log(person1);
// console.log(person2);

// console.log(person1);
// console.log(person1.dob);
// console.log(person1.dob.getDay());
// console.log(person1.dob.getMonth());
// console.log(person1.dob.getFullYear());
// console.log(person1.getBirthYear());
// console.log(person1.getFullName());
//
// console.log(person1.getBirthYear2());


// class Person {
//     constructor(firstName, lastName, dob) {
//         this.firstName = firstName;
//         this.lastName = lastName;
//         this.dob = new Date(dob);
//     }
//
//     getBirthYear(){
//         return this.dob.getFullYear();
//     }
//
//     getFullName(){
//         return `My name is: ${this.firstName} ${this.lastName}.`
//     }
// }
//
// const person1 = new Person('Moti', 'Katz', '4-3-1980');
// console.log(person1);
// console.log(person1.dob);
// console.log(person1.dob.getDay());
// console.log(person1.dob.getMonth());
// console.log(person1.dob.getFullYear());
// console.log(person1.getBirthYear());
// console.log(person1.getFullName());


// console.log(window);
// window.console.log('');
// // console.log(window.innerHeight);
// // console.log(window.innerWidth);
// window.localStorage['my_secret_name'] = 'abc';
// console.log(window.localStorage);
//
// console.log(window.document);

// console.log(document.getElementById('my-form'));
// const myForm = document.getElementById('my-form');
// console.log(myForm);

// console.log(document.getElementsByClassName('item'));
// console.log(document.getElementsByTagName('li'));

// console.log(document.querySelector('#my-form'));
// console.log(document.querySelector('.item'));
// console.log(document.querySelectorAll('.item'));
// console.log(document.querySelector('li'));
// console.log(document.querySelectorAll('li'));
//
// const items = document.querySelectorAll('.item');
// items.forEach(item => console.log(item));

// const ul = document.querySelector('.items');
// console.log(ul);
// // ul.remove();
// // ul.lastElementChild.remove();
// // ul.lastElementChild.textContent = 'Hello!'
// ul.children[1].innerText = '<h1>Brad is my friend!</h1>';
// ul.children[2].innerHTML = '<h1>Brad is my friend!</h1>';
//
// const btn = document.querySelector('.btn');
// btn.style.background = 'red';
// btn.style.color = 'white';


// const btn = document.querySelector('.btn');
// // btn.addEventListener('click', (e) => {
// //     e.preventDefault();
// //     console.log('click!!!');
// // })
// let color_bool = true;
// btn.addEventListener('click', (e) => {
//     e.preventDefault();
//     // console.log(e);
//     // console.log(e.target);
//     // console.log(e.target.className);
//     e.target.style.background = color_bool ? 'red': 'green';
//     color_bool = !color_bool;
//     // document.querySelector('body').style.background = '#333';
//     // document.querySelector('body').style.color = 'white';
//     // document.querySelector('.items').lastElementChild.remove();
// })

// btn.addEventListener('mouseover', (e) => {
//     document.querySelector('body').style.background = '#333';
//     document.querySelector('body').style.color = 'white';
// })
//
// btn.addEventListener('mouseout', (e) => {
//     document.querySelector('body').style.background = 'white';
//     document.querySelector('body').style.color = 'black';
// })


/////////////////////////////
// Form Validation Example
/////////////////////////////


const myForm = document.querySelector('#my-form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const msg = document.querySelector('.msg');
const usersList = document.querySelector('.users');

const onSubmit = (e) => {
    e.preventDefault();
    // console.log(nameInput.value);
    // console.log(emailInput.value);
    if (nameInput.value === '' || emailInput.value === '') {
        // msg.innerHTML = '<h3>Please enter all fields!</h3>'
        msg.innerHTML = 'Please enter all fields!'
        msg.classList.add('error');
        setTimeout(() => {
            msg.innerHTML = '';
            msg.classList.remove('error');
        }, 2000);
    } else {
        const li = document.createElement('li');
        li.innerText = `${nameInput.value}: ${emailInput.value}`
        usersList.appendChild(li);
        nameInput.value = '';
        emailInput.value = '';
        // msg.innerHTML = '';
        // msg.classList.remove('error');

    }
}

myForm.addEventListener('submit', onSubmit);

























console.log('----------------')
