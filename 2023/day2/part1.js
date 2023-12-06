const RED_CUBES_TOTAL = 12
const GREEN_CUBES_TOTAL = 13
const BLUE_CUBES_TOTAL = 14

const fs = require('fs');

const readFileLines = filename => fs.readFileSync(filename).toString('UTF8').split('\n');

const lines = readFileLines('input.txt');
let result = []
for(const line of lines){
  const stripGameOut = line.split(': ')
  for(const game of stripGameOut) {
    if(!game.includes('Game')){
      let level = []
      const sets = game.split('; ')
      for(const set of sets){
        let set_results = {}
        const values = set.split(', ')
        for(const value of values) {
          const [colorCount, color] = value.split(' ')
          set_results[color] = colorCount
        }
        level.push(set_results)
      }
      result.push(level)
    }
  }
}

function isOutOfRange(key, value) {
  switch (key) {
    case 'red':
      if(value > RED_CUBES_TOTAL) return true
      break;
    case 'green':
      if(value > GREEN_CUBES_TOTAL) return true
      break;
    case 'blue':
      if(value > BLUE_CUBES_TOTAL) return true
      break;
    default:
      throw new Error('Unexpected key received')
  }
  return false
}
let result_boolean = []
for(const round of result) {
  let level = []
  for(const set of round) {
    let currentValue;
    let falseFlag = false;
    for (const [key, value] of Object.entries(set)) {
      currentValue = isOutOfRange(key, value)
      if(currentValue) {
        level.push(false);
        falseFlag = true
        break;
      }
    }
    if(!falseFlag) level.push(true)
  }
  result_boolean.push([level])
}
let sum = 0
let round = 1

for (const results of result_boolean) {
  for (const result of results) {
    if(!result.includes(false)) {
      sum += round
    }
  }
  round++
}
console.log(sum)