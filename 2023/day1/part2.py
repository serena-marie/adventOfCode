from pathlib import Path

NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def readFile(filename):
  file_path = Path(__file__).parent / filename

  with open(file_path, 'r') as file:
    strings = file.read().split('\n')
    words = [word for word in strings]
    return words

def parseWord(word):
  foundMatches = []
  for start in range(len(word)):
    for end in range(start + 1, len(word) + 1):
      current_substring = word[start:end]

      if current_substring in NUMBERS:
        foundMatches.append(str(NUMBERS.index(current_substring)+1));
        break;
      elif len(current_substring) == 1 and current_substring.isnumeric():
        foundMatches.append(str(current_substring))

  if(len(foundMatches) > 1):
    firstVal = foundMatches[0]
    lastVal = foundMatches[-1]
  else:
    firstVal = foundMatches[0]
    lastVal = firstVal

  result = firstVal + lastVal
  return result

def parseWords(words):
  results = []
  for word in words:
    results.append(parseWord(word))
  return results

def calculateSum(calibValues):
  sum_result = 0
  for num in calibValues:
    sum_result += int(num)
  return sum_result
      
try:
  words = readFile('mini_input2.txt')
  calibValues = parseWords(words)
  print(calculateSum(calibValues))
except FileNotFoundError as e:
  print(f'Error! File not found. ==> {e}')