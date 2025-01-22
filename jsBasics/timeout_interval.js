// setTimeout
// If you want to run something after 5 seconds, use setTimeout
// setInterval
// If you want to run something every 5 seconds, use setInterval

// let count = 0;
// let secondOption = () => {
//     console.log('Hi my name is David')
//     count++;
// 
//     if(count === 5){
//         clearInterval(secondOption);
//         console.log('Interval stopped after 5 iterations')
//     }
// }
// 
// setInterval(secondOption, 5000)

// const intervalID = setInterval(() => {
//     console.log('Hi my name is David')
//     count++;
// 
//     if(count === 5){
//         clearInterval(intervalID);
//         console.log('Interval stopped after 5 iterations')
//     }
// }, 5000); // 5000 milliseconds is 5 seconds

// setInterval does not stop after clearing the interval in ther function using a counter

// function displayMessage(){
//     console.log('Hi my name is David')
// }
// 
// setTimeout(displayMessage, 3000)


let counter = 0

function greet(){
    counter++
    console.log('Hello this is ' + counter + ' iteration')

    if(counter == 3){
        clearInterval(intervalID)
        console.log('Intervals Stopped')
    }
}
const intervalID = setInterval(greet, 1000)