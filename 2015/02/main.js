const fs = require('fs');

function load_input(filename = 'input.txt'){
 try {
  const data = fs.readFileSync('input.txt', 'utf8');
  return data
} catch (err) {
  console.error(err);
    }
}

function sort_dimensions(input_data){
    let sorted_dimensions = input_data.split('\n').map(string => string.split('x').sort((a,b) =>a-b))
    return sorted_dimensions
}

function wrap (dimensions){
    return (3 * dimensions[0]* dimensions[1] + 2 * dimensions[0]* dimensions[2] + 2 * dimensions[2]* dimensions[1])
}
function ribbon (dimensions){
    return 2 * dimensions[0] + 2 * dimensions[1] + dimensions.reduce((a,b) => a*b)
}
const input_data = load_input()
let sorted = sort_dimensions(input_data)
console.log('---PART ONE--')
console.log(sorted.map(element => wrap(element)).reduce((a,b) => a+b))
console.log('---PART TWO--')
console.log(sorted.map(element => ribbon(element)).reduce((a,b) => a+b))