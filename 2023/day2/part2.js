const RED_CUBES_TOTAL = 12
const GREEN_CUBES_TOTAL = 13
const BLUE_CUBES_TOTAL = 14

const fs = require('fs');
const path = require('path');
const readFileLines = filename => fs.readFileSync(filename).toString('UTF8').split('\n');

const lines = readFileLines(path.join(__dirname, 'input/mini_input1.txt'));

/**
 * Parse lines from files to build an object with the results of each set
 */
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

/***
 * Calculate the sum of the game IDs where the game was possible
 */
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

console.log(`Answer part 1: ${sum}`)

// console.log(`result ${JSON.stringify(result)}`)

/**
 * Loop through result to grab max of each set
 */
const maxOfEachRound = []
for (const currentRound of result) {
  const testResults = currentRound.reduce((prevVal, currentVal) => {
    Object.entries(currentVal).forEach(([color, colorCount]) => {
      prevVal[color] = Math.max(prevVal[color], colorCount)
    });
    return prevVal;
  }, {
    'red': 0,
    'green': 0,
    'blue': 0
  })
  maxOfEachRound.push(testResults)
}

/**
 * Loop through each game to determine if possibe
 */
// let result_boolean2 = []
// for(const round of result) {
//   let level = []
//   for(const set of round) {
//     let currentValue;
//     let falseFlag = false;
//     for (const [key, value] of Object.entries(set)) {
//       currentValue = isOutOfRange(key, value)
//       if(currentValue) {
//         level.push(false);
//         falseFlag = true
//         break;
//       }
//     }
//     if(!falseFlag) level.push(true)
//   }
//   result_boolean2.push([level])
// }
// console.log(result_boolean2)

/***
 * Calculate the sum of the game IDs where the game was possible
 */
// let sum2 = 0
// let round2 = 1
// let possibleGamePowers = []
// for (const results of result_boolean2) {
//   for (const result of results) {
//     if(!result.includes(false)) {
//       const currentRoundMaxes = maxOfEachRound[round2-1] //{ red: 4, green: 2, blue: 6 }
//       const result = Object.values(currentRoundMaxes).reduce((prevVal, currentVal) => {
//         return prevVal *= currentVal;
//       }, 1)
//       possibleGamePowers.push(result)
//     }
//   }
//   round2++
// }

/**
 * Calculate power of each round
 */
let powerOfRounds = 0
for(const round of maxOfEachRound){
  const result = Object.values(round).reduce((prevVal, currentVal) => {
    return prevVal *= currentVal
  }, 1)
  powerOfRounds += result
}
console.log(`Answer part 2: ${powerOfRounds}`)
// console.log(`Answer part 2: ${JSON.stringify(maxOfEachRound, null, 2)}`)