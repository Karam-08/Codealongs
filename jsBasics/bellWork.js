let scores = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

let a, b, c, d, e, f, g, h, i, j, k = scores

// The process of using ES6 shortcuts and functions
// 1: Arrow functions

function getScores(){
    let [a, b, c, d] = [1, 2, 3, 4]
}

// function getScores2 = (x) =>{
//     let [a, b, c, d] = [1, 2, 3, 4]
//     console.log(a)
// }

// getScores2("HI")

let obj = {
    names:['tim', 'tia', 'jim', 'pam', 'dwight'],
    games:['A', 'B', 'C', 'D', 'F'],
    scores:{
        tim: '90',
        tia: '80',
        jim: '60',
        pam: '80',
        dwight: '70'
    }
}

console.log(["Bernard", "Spruce Goose Bruce", ...obj.names])

let newObj={
    names:{
        ...obj.names
    }
}

console.log(newObj)