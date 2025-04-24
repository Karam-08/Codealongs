// Create an array with 4 items. Use array destructuring to store the first two items into separate variables.
let arr1 =  [1, 2, 3, 4]
let [a, b] = [arr1[0], arr1[1]]

console.log(a, b)

// Create an object with 3 properties of your choice. Use object destructuring to access each property.
let person1 = {
    names: 'Karam',
    age: 17,
    city1: 'Arizona'
}

let {names, age, city1} = person1

console.log(names)
console.log(age)
console.log(city1)

// Create a function that accepts an object with properties x and y, and returns the result of x + y using destructuring inside the function.

function add({x, y}){
    return x + y
}

let result = add({x: 9, y: 10});
console.log(result)

// Challenge (Extra Credit)
// Given the following object, use nested destructuring to extract the values of city and zip:

const person2 = {
    name: "Jake", 
    address: { 
        city2: "Phoenix", 
        zip: "85001" 
    }};

let {address: {city2, zip}} = person2
// extracts city2 and zip from the address object

console.log(city2)
console.log(zip)