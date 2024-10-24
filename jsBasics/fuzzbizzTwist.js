for(var i = 1; i < 51; i++){
    if(i % 5 === 0 && i % 3 === 0){
        console.log("FizzBuzz");
        continue
    }else if(i % 5 === 0){
        console.log("Buzz");
        continue
    }else if(i % 3 === 0){
        console.log("Fizz")
        continue
    }
console.log(i)
}

for(var i = 1; i < 51; i++){
    switch(i){
        case (i % 5 === 0 && i % 3 === 0):
            console.log('FizzBuzz')
            break;
        case (i % 5 === 0):
            console.log('Buzz')
            break;
        case (i % 3 === 0):
            console.log('Fizz')
            break;
        default:
            console.log(i)
    }
}