let park ="Disney"
//Camel Case Example
let firstName = "Karam"
let lastName = "Abbas"
console.log(firstName)
console.log(park)
console.log(typeof lastName)

let message = `this is a message saying that
you should do better at driving`
console.log(message)

let myname = 'Karam'
let age = 16
let alive = true
let favFoods = ['italian', + 'japanese' , 'arabian']
console.log(myname + ' '  + age + ' ' + alive + ' ' + favFoods)

let test = 4
console.log("The value of test is: " + test + "")

let favMovie = 'Back To The Future'
let favGame = 'Dead Space'

console.log(String(null))  
console.log(String(true))  
console.log(String(84)) 

console.log(myname + ' '  + age + ' ' + alive + ' ' + favFoods + ' ' + favMovie + ' ' + favGame)

console.log(Number(true)) 
console.log(Number(false)) 

console.log(Number(4526))

console.log(Number(null))

console.log(Number(""))

let age1 = 23, age2 = 56

if(age2 > 45){
    console.log("They OLD!")
}
else if(age1 < 30){
    console.log("Babies am I right?")
}
else{
    console.log("They are getting there.")
}

let bf = "Jesse Pinkman"
let thinksBF = "Badger Mayhew"

if(bf == thinksBF){
    console.log("You need more Friends.")
}

if(bf != thinksBF){
    console.log("You must have plenty of Friends.")
}

if(15 == "15"){
    console.log("You can read. Congrats.")
}

if(15 === "15"){
    console.log("You can read. Congrats.")
}

if("15" === "15"){
    console.log("You can read. Congrats.")
}

let Alive = true
let year = 2020

if(year == 2024){
    if(alive = true){
        console.log("Yay!")
    }
    console.log("Level 1")
}

let $ = 40

if($ < 21){
    console.log("Broke Netflix")
}
else if(22 < $ < 61){
    console.log("Movie Theatre")
}
else if(62 < $ < 81){
    console.log("Dinner")
}

else if(82 < $ < 150){
    console.log("Sky Diving")
}

let num = 257
// alert("This is proof") //
console.log("I will live until I'm" + num)

let test1 = "Bored"
let test2 = "bored"

// console.log(Object.is(test1, test2))

console.log(5 > 4)
console.log("apple" > "appear")
console.log("west" < "Went")
console.log(2 > "12")
console.log(undefined == null)
console.log(undefined === null)
console.log(null == "0")

if(year == 2020) console.log('uh-oh');

if(true)console.log('works')
if(0)console.log('doesnt work')

let check = "false"
if(check) console.log('this works too')

let age4 = 24
let canDrink = console.log((age4 >= 21) ? true : false)

let a = 1
let b = 3

console.log((a + b < 4) ? 'Below' : 'Over')

let grade = 81

if(grade > 90){
    console.log('A')
} else if (grade > 80){
    console.log('B')
} else if (grade > 70){
    console.log('C')
} else if (grade > 60){
    console.log('D')
} else {
    console.log('You Suck')
}

let answer = "45"
switch(answer){
    case"left":
        console.log("You're going left")
        break;
    case"right":
        console.log("You're going right")
        break;
    default:
        console.log("You're going forward")
}

let message1;

let login = "employee"
switch(login){
    case "employee":
        message1 = 'Hello';
        break;
    case "director":
        message1 = 'Greetings';
        break;
    case "":
        message1 = 'No Login';
        break;
    default:
        message1 = '';
}
console.log(message1)

let pen = true
let paper = true
let mouse = false
let keyboard = true

if(pen && paper == true || mouse && keyboard == true){
    console.log('You can take notes')
} else {
    console.log('You cannot take notes')
}

let allNighter = false
let didNotStudy = false
let tooManyGames = false
let skippedBreakfast = false

if(!allNighter && !tooManyGames && !didNotStudy && !skippedBreakfast){
    console.log('Bro is locked in fr fr')
} else {
    console.log('Bro is so cooked lmao')
}

let location = null
let geoLocation;

console.log(geoLocation ?? 'Not a valid geo location')
let newLocation = location ?? 'Arizona'
console.log(newLocation)

let number1 = Math.floor(Math.random() * 100)
let number2 = Math.floor(Math.random() * 100)
let number3 = Math.floor(Math.random() * 100)
let number4 = Math.floor(Math.random() * 100)
let number5 = Math.floor(Math.random() * 100)

console.log(number1 + ',', number2 + ',', number3 + ',', number4 + ',', number5)

for(var i = 10; i > 1; i--){
    console.log(`This has happened ${i} times`)
}

for(var i = 5; i < 14; i+= 2){
    console.log(i)
}

for(var i = 5; i < 12; i++){
    console.log(i)
}

console.log('---------------------')

for(var i = 1; i < 10; i++){
    console.log("this is nice")
}

console.log('---------------------')

for(var i = 11; i > 0; i-=2){
    console.log(i)
}

let i = 0;
while(i < 3){
    console.log(i);
    i++;
}

let i = 0;
do{
    console.log(i);
    i++;
} while (i < 3)

var classes = 12

for(var i = 0; i < classes; i++){
    if(i==7){
        console.log("The next frontier")
        continue
    }
    console.log(i)
    console.log("This should always print")
}

outer: for(var i = 0; i < 3; i++){
    for(var j = 0; j < 5; j++){
        let input = prompt("What is your name?")
        if(input.length > 0){
            break outer;
        }
    }
}