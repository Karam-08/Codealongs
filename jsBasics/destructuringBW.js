// 1: What is destructuring in JavaScript?
// A. Assigning values to variables from an array or object. // This is the answer
// B. Creating a new array.
// C. Combining objects into one.
// D. Declaring variables. 

// 2: What is the result of the following destructuring operation?

// const [first, second] = [10, 20];
// A. first = 10, second = 20 // This is the answer
// B. first = undefined, second = undefined
// C. first = 10, second = undefined
// D. first = 20, second = 10


// 3: Use destructuring to assign the values from this object to variables.

const person1 = {names: 'John', age: 30, city: 'New York'};
// Assign name to a variable personName, age to a variable personAge, and city to a variable personCity.
let {names: personName, age: personAge, city: personCity} = person1
console.log(personCity)
// 4: What would be the output of this code?

// const { a, b, c } = { a: 5, b: 10 }; console.log(a, b, c);
// A. 5 10 undefined // This is the output
// B. undefined undefined undefined
// C. 5 10 10
// D. undefined undefined 10


// 5: Given the following array of objects, use destructuring to extract the name and age of each person and log them.

const people = [{names: 'Alice', age: 25, city: 'Paris'}, {names: 'Bob', age: 30, city: 'London'}, {names: 'Charlie', age: 35, city: 'Berlin'}];
// Use a loop or array method to log the name and age of each person.
for(var i = 0; i < people.length; i++){
    let{peopleNames: names, peopleAge: age} = people
    console.log(peopleNames)
}


// 6: Use destructuring with a default value for the city property in the following object. If city is not present, assign it a default value of 'Unknown'.

const person2 = {name: 'Eve', age: 40};

// 7: You have the following nested object:

const employee = {id: 1234, personalInfo: {name: 'John Doe', age: 28}, jobDetails: {position: 'Software Engineer', department: 'Development'}};
// Use destructuring to extract the name from personalInfo, the position from jobDetails, and the id from the top level.

// 8: Given this function that returns an object, use destructuring to get the title and author properties. Provide a default value for author if it is missing.

function getBookInfo(){
    return {title: '1984', name: 'George Orwell'}; // Missing author
}