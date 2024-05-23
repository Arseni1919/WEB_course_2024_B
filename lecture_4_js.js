// alert('inside lecture 4!')

// console.log('this is a console message!')
// console.warn('this is a warning message!')
// console.error('this is an error message!')

// let age = 39;
// age = 'hi';
// console.log(age)

// const age = 39;
// // age = 40;
// console.log(age)

// const message = 'hi!';
// console.log(message);
// const x = 3;
// const x2 = 3.0;
// const y = 3.5;
// console.log(x);
// console.log(x2);
// console.log(y);
// const is_free = true;
// let my_age = null;
// let my_age = 40;
// console.log(my_age);
// console.log(typeof my_age);

// let x = 50;
// let y = 3;
// x %= y;
// console.log(x)

// const name = 'Ariel';
// const age = 100;
// // console.log('My name is ' + name + ' and I am ' + age + '!')
// // console.log(`My name is ${name} and I am ${age}!`)
// // console.log(`''''' """" ${name} -> ${age + 23}`)
//
// const my_message = `my name is ${name} ...`


// const s = 'Hello World!';
// console.log(s.length);
// console.log(s.toUpperCase());
// console.log(s.toLowerCase());
// console.log(s.substring(0, 7));
// console.log(s.substring(0, 7).toUpperCase());
// console.log(s.split(''));

// const numbers = [1, 2, 3, 4];
// numbers[0] = 'apples';
// console.log(numbers[30]);
// const arr1 = [1, 'apple', true]
// console.log(arr1)

// const fruits = ['apple', 'orange', 'banana'];
// fruits[4] = 'grapes';
// fruits.push(null);
// fruits.unshift('melon');
// fruits.pop();
// console.log(fruits);
//
// console.log(`this is ${Array.isArray(fruits)}`)
// // console.log(Array.isArray('hi'))
//
// console.log(fruits.indexOf('banana'));


const person = {
    firstName: 'John',
    lastName: 'Doe',
    age: 30,
    hobbies: ['music', 'movies', 'sports'],
    address: {
        street: '50 main st',
        city: 'Boston',
        state: 'MA'
    }
};

// console.log(person);
// console.log(person.firstName);
// console.log(person.hobbies[1]);

// const {firstName, lastName, address: {city}} = person;
// console.log(firstName);
// console.log(lastName);
// console.log(city);

// person.email = 'john@gmail.com';
// console.log(person);

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
// console.log(todos);
// const todosJSON = JSON.stringify(todos);
// console.log(todosJSON);
// const recovered_todos = JSON.parse(todosJSON);
// console.log(recovered_todos);


// for (let i = 0; i < 10; i++) {
//     console.log(`FOR loop number: ${i}`)
// }
//
// let i = 0;
// while(i < 10) {
//     console.log(`WHILE loop number: ${i}`)
//     i++;
// }

for(let i = 0; i < todos.length; i++) {
    console.log(todos[i].text);
}

for (let todo of todos){
    console.log(todo.text);
}

todos.forEach(function(todo){
    console.log(todo.text);
})

const todoText = todos.map(function(todo){
    return todo.text;
})
console.log(todoText);

const todoCompleted = todos.filter(function (todo) {
    return todo.isComplete;
})
console.log(todoCompleted);

const todoCompletedText = todos.filter(function (todo) {
    return todo.isComplete;
}).map(function(todo){
    return todo.text;
})
console.log(todoCompletedText);








console.log('---------------------')

