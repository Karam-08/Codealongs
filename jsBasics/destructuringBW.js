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

const person1 = {name1: 'John', age: 30, city: 'New York'};
// Assign name to a variable personName, age to a variable personAge, and city to a variable personCity.
let {name1: personName, age: personAge, city: personCity} = person1
console.log(personCity)


// 4: What would be the output of this code?

// const { a, b, c } = { a: 5, b: 10 }; console.log(a, b, c);
// A. 5 10 undefined // This is the output
// B. undefined undefined undefined
// C. 5 10 10
// D. undefined undefined 10


// 5: Given the following array of objects, use destructuring to extract the name and age of each person and log them.

const people = [{name2: 'Alice', age: 25, city: 'Paris'}, {name2: 'Bob', age: 30, city: 'London'}, {name2: 'Charlie', age: 35, city: 'Berlin'}];
// Use a loop or array method to log the name and age of each person.
for(var i = 0; i < people.length; i++){
    let{name2, age} = people[i]
    console.log(name2, age)
}


// 6: Use destructuring with a default value for the city property in the following object. If city is not present, assign it a default value of 'Unknown'.
const person2 = {name3: 'Eve', age: 40};

let {name3, age, city = 'Unknown'} = person2
// Unknown is the default value if city is not defined in the object
console.log(name3)
console.log(age)
console.log(city)


// 7: You have the following nested object:

const employee = {id: 1234, personalInfo: {name4: 'John Doe', age: 28}, jobDetails: {position: 'Software Engineer', department: 'Development'}};
// Use destructuring to extract the name from personalInfo, the position from jobDetails, and the id from the top level.
let {id, personalInfo: {name4}, jobDetails: {position}} = employee
console.log(name4)
console.log(position)
console.log(id)


// 8: Given this function that returns an object, use destructuring to get the title and author properties. Provide a default value for author if it is missing.

function getBookInfo(){
    return {title: '1984'}; // Missing author
}

// Destructures the returned object and sets a default for author
let {title, author = 'Unknown'} = getBookInfo();

console.log(title)
console.log(author)