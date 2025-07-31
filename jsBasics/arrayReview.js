// Code-A-Long Basic Array Methods

//=============================================================
//  STARTER DATA
//=============================================================
const students = [
    {name:'Marcus', gpa:3.8},
    {name:'Jessica', gpa:4.0},
    {name:'Chen', gpa:3.5},
    {name:'Maria', gpa:3.9},
]

const seniorActivities = ['Prom Committee', 'Yearbook', "Student Council"]

// ================================
// Adding and Removing Elements
// Methods: push(), pop(), shift(), unshift()

console.log('----Section 1: Adding and Removing----')

// We are going to add a new student to our class
console.log("Original students array:", students)
students.push({name: "Ethan", GPA: 3.7})
console.log("After push():", students)

// One student is being transferred out of the school so we will shift() to remove the first element for the students array
// We'll store the removed item to see who left
const earlyTransfer = students.shift()
console.log('\nStudents who transferred: ', earlyTransfer.name)
console.log('After Shift():', students)

// Let's add the Senior trip to the list of Senior activities
// We'll use unshift() to add this activity to the beginning of the array
console.log('\nOriginal Senior Activiites', seniorActivities)
seniorActivities.unshift("Senior Trip")
console.log("After unshift():", seniorActivities)

// We use pop() to remove the last element from the 'seniorActivities' array.
const cancelledActivity = seniorActivities.pop();
console.log('\nCancelled Activity:', cancelledActivity);
console.log('After pop():', seniorActivities)

// ==================================================
// Section 2: Combining and Formatiing
// Methods: concat(), join(), toString()
// ==================================================

console.log('\n----Section 2: Combining & Formatting----')

// We use concat() to combine the existing 'seniorActivities' with a new array.
// The 'seniorActivities' array remains unchanged
const combinedActivities = [...seniorActivities, 'Drama Club', 'Robotics'];
// const combinedActivities = seniorActivities.concat(newActivities);
console.log('Original Senior Activities:', seniorActivities)
console.log('Combined Activities list:', combinedActivities)

// We use join() to create a single string from the 'combinedActivities' array.
// We can specify a seperator, like a hyphen, to customize the output.
const websiteDisplay = combinedActivities.join(' -> ');
console.log('\nWebsite display string:', websiteDisplay)

// We use toString() which is similar to join, but always uses a comma as a seperator
const rawString = seniorActivities.toString();
console.log('\n Original activities as a string:', rawString)
// Notice the difference: join() gives you control over the seperator while toString() is a default behavior

// ======================================
// Section 3: Finding and Ordering
// Methods: slice(), find(), sort()
// slice() and find() are non-destructive, sort() is destructive.

console.log('\n----Section 3: Finding & Ordering----')

// We use find() to search for an object in the students array where the GPA is 4.0
// find() returns the first object that matches the condition
const valedictorian = students.find(student => student.gpa === 4.0);
console.log('Valedictorian found:', valedictorian)

// We use slice(0, 2) to get the first two elements.
// This creates a NEW array and does not change the original 'students' array.
const honorRoll = students.slice(0, 2);
console.log('\nOriginal Students array', students)
console.log('Honor roll students (slice)', honorRoll)

// We'll use a compare function to sort the objects by their 'name' property.
// const studentsCopy = [...students]; // A quick way to make a shallow copy
// studentsCopy.sort((a, b) => {
//     if(a.name < b.name) return -1;
//     if(a.name > b.name) return 1;
//     return 0;
// });
// array.sort(function(a, b){return b.name-a.name})
// console.log('Sorted: ', array)
// console.log('\nOriginal students array (unchanged)', students);
// console.log('\nStudents sorted alphabetically', studentsCopy)


console.log('\n---Section 4: Bonus Challenge---')
const studentsCopy2 = [...students]
studentsCopy2.sort((a, b) =>{
    if(a.name < b.name) return -1;
    if(a.name > b.name) return 1;
    return 0;
});
console.log(studentsCopy2)
organizedStudents = []
for(var i = 0; i < studentsCopy2.length; i++){
    organizedStudents.push(studentsCopy2[i].name)
}
const seperatedStudents = organizedStudents.join(" | ")
console.log(seperatedStudents)