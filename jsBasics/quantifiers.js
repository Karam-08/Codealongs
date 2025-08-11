// "?" makes the preceding character or group optional, matching it zero or one time
const str = 'color colour'
const pattern  = /colou?r/g

let matches = str.match(pattern)
console.log(matches)


// the + matches the preceding character or group one or more times. It's useful for finding patterns with repetition
const str2 = "The number 1, is not 111, or 1"
const pattern2 = /1+/g
// g stands for global which gives every repetition instead of only the first one
let matches2 = str2.match(pattern2)
console.log(matches2)

// It finds all three groups of 1s because they all contain one or more consecutive 1s


// "*" matches the preceding character or group zero or more times. It's avery flexible quantifier that can be used to find patterns with or without the character
const str3 = "A cat sat on the mat. Caat sat on the maaaaat. C sat on the m@t. Spelling cat ct"
const pattern3 = /ca*t/gi
// the i flag is for the search using case insensitivity
const matches3 = str3.match(pattern3)
console.log(matches3)
// m@t does not work because there is no a nor is there an empty space

// let digits = "1234567890"
// console.log(digits.match(/\d{3}/))
// console.log(digits.match(/\d{5,}/))

let email = "test@example.com"
let pattern4 = /^test/; // Matches 'test' at the beginning
let pattern5 = /com$/; // Matches 'com' at the end

let year = "2008"
let yeardigits = /\d{4}/g

const matches4 = year.match(yeardigits)
console.log(matches4)