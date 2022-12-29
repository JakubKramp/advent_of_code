const fs = require('fs');

const repeat = /(\w)\1+/
const pairs = /((\w)\w).*\1/
const sandwich= /(\w)(\w)\1/
const forbidden = ['ab', 'cd', 'pq', 'xy']
const vowels = ['a', 'e', 'i', 'o', 'u']

function load_input(filename = 'input.txt') {
 try {
  const data = fs.readFileSync('input.txt', 'utf8');
  return data
} catch (err) {
  console.error(err);
    }
}

function is_nice(text){
    let counter = 0
    for(substring of forbidden){
        if (text.includes(substring)){
            return false
        }
    }
    for(char of text) {
        if (vowels.includes(char)) {
            counter += 1
        }
    }
    if (counter<3){
                return false
        }
    return repeat.test(text)
}

function new_nice(text){
    return (sandwich.test(text) && pairs.test(text))
}


let input_data = load_input()
console.log('---PART ONE--')
console.log(input_data.split('\n').map(is_nice).filter(elem => elem == true).length)
console.log('---PART TWO--')
console.log(input_data.split('\n').map(new_nice).filter(elem => elem == true).length)

