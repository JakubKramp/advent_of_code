
// Node.js program to demonstrate the
// fs.open() Method

// Include the fs module
const fs = require('fs');

function load_input(filename = 'input.txt'){
 try {
  const data = fs.readFileSync('input.txt', 'utf8');
  return data
} catch (err) {
  console.error(err);
}
}

const input_data = load_input()

function get_floor(instructions){
    let floor = 0
    for (let i of instructions){
        switch (i){
            case '(':
                floor += 1
                break;
            case ')':
                floor -= 1
                break;
        }
    }
    return floor
}
function get_basement_entrance(instructions){
    let floor = 0
    for (let i=0; i<instructions.length; i++){
        switch (instructions[i]){
            case '(':
                floor += 1
                break;
            case ')':
                floor -= 1
                if (floor<0){
                    return i + 1
                }
                break;
        }
    }
}
console.log("---PART ONE---")
console.log(get_floor(input_data))
console.log("---PART TWO---")
console.log(get_basement_entrance(input_data))
