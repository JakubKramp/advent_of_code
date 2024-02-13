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
    checksum = 0
    let lines = input_data.split("\n")
    for (let i= 0; i < lines.length; i++) {
        numbers = lines[i].split("\t")
        numbers = numbers.map(function(str) {
    return parseInt(str, 10);
});
        checksum += Math.max(...numbers)- Math.min(...numbers)
    }
    return checksum
}

function part_two(input_data) {
    checksum = 0
    let lines = input_data.split("\n")
    for (let i= 0; i < lines.length; i++) {
        numbers = lines[i].split("\t")
        numbers = numbers.map(function (str) {
            return parseInt(str, 10);
        })
        for (let j = 0; j < numbers.length; j++) {
            for (let h = 0; h < numbers.length; h++) {
                if (numbers[j] % numbers [h] === 0 && numbers[j] !== numbers[h]) {
                    checksum += numbers[j] / numbers [h]
                }

            }
        }
    }
    return checksum
}

console.log("---PART ONE---")
console.log(part_one(input_data))
console.log("---PART TWO---")
console.log(part_two(input_data))
