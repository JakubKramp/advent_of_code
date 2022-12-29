const fs = require('fs');

function load_input(filename = 'input.txt'){
 try {
  const data = fs.readFileSync('input.txt', 'utf8');
  return data
} catch (err) {
  console.error(err);
    }
}

function visit_houses(input_data, santas_count=1){
    let santa_positions = new Array()
    let houses_visited = new Set()
    for (let i=0; i<santas_count; i++){
        santa_positions.push(new Array(0,0))
    }
    for (let i=0; i<input_data.length; i++){
        let santa_position = santa_positions[i%santas_count]
        switch (input_data[i]){
            case '>':
                santa_position[0]+=1
                houses_visited.add(JSON.stringify(santa_position))
                break;
            case '<':
                santa_position[0]-=1
                houses_visited.add(JSON.stringify(santa_position))
                break;
            case '^':
                santa_position[1]+=1
                houses_visited.add(JSON.stringify(santa_position))
                break;
            case 'v':
                santa_position[1]-=1
                houses_visited.add(JSON.stringify(santa_position))
                break;
        }
    }
    return houses_visited.size
}

let input_data = load_input()
console.log('---PART ONE--')
console.log(visit_houses(input_data))
console.log('---PART TWO--')
console.log(visit_houses(input_data, 2))