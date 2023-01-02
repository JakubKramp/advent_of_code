const fs = require("fs");

function initialize_board(size = [1000,1000], bool= true){
    let cols = size[0]
    let rows = size[1]
    let array = [];
    let value
    if (bool){
        value = false
    }
    else value = 0
    for (let i = 0; i < rows; i++) {
      array.push(new Array(cols).fill(value));
    }
    return array
}

function load_input(filename = 'input.txt') {
 try {
  const data = fs.readFileSync('input.txt', 'utf8');
  return data
} catch (err) {
  console.error(err);
    }
}


function execute_command(command) {
    let x = []
    let y = []
    const regex = /(\d+),(\d+).*(\d+),(\d+)/
    for (let coordinates of command.match(regex)[0].split('through')) {
        x.push(coordinates.split(',')[0]), y.push(coordinates.split(',')[1])
    }
    if (command.startsWith('turn on')) {
        for (let i = x[0]; i < x[1]; i++) {
            for (let j = y[0]; j < y[1]+1; j++) {
                board[i][j] = true
            }
        }
    } else if(command.startsWith('turn off')){
        for (let i = x[0]; i < x[1]; i++) {
            for (let j = y[0]; j < y[1]+1; j++) {
                board[i][j] = false
            }
        }
    }else if(command.startsWith('toggle')) {
        for (let i = x[0]; i < x[1]; i++) {
            for (let j = y[0]; j < y[1] + 1; j++) {
                board[i][j] = !board[i][j]
            }
        }
    }
    return
}


let input_data = load_input()
let board = initialize_board()
console.log('---PART ONE--')
console.log(input_data.split('\n').map(execute_command))