const fs = require('fs');
function load_input(filename = 'input.txt'){
 try {
     return fs.readFileSync('input.txt', 'utf8')
    }
catch (err) {
  console.error(err);
    }
}
const input_data = load_input()


function part_one(input_data) {
    sum = 0
    for (let i = 0; i < input_data.length; i++) {
        if (input_data[i] === input_data[i + 1]) {
            sum += parseInt(input_data[i])
        }
    }
        if (input_data[0] === input_data[input_data.length - 1]){
            sum += parseInt(input_data[0])
    }
    return sum
}


function part_two(input_data) {
    let sum = 0
    let half = parseInt(input_data.length/2)
    for (let i = 0; i < half; i++) {
        if (input_data[i] === input_data[i + half]) {
            sum += parseInt(input_data[i])
        }
    }
    return sum*2
}

console.log("---PART ONE---")
console.log(part_one(input_data))
console.log("---PART TWO---")
console.log(part_two(input_data))

