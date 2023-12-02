from pathlib import Path

def readFile(filename):
  file_path = Path(__file__).parent / filename

  with open(file_path, 'r') as file:
    strings = file.read().split('\n')
    words = [word for word in strings]
    return words

def findCalibrationValue(words):
  values = []
  
  for word in words:
    calibValue = ''
    lastNum = ''
    for char in word:
      if char.isnumeric():
        if lastNum == '':
          calibValue = char
          lastNum = char
        else:
          lastNum = char
    # Add to the list
    calibValue = calibValue + lastNum
    values.append(calibValue)
  return values

def calculateCalibrationSum(calibrationValueList):
  sum = 0
  for number in calibrationValueList:
    sum = sum + int(number)
  return sum
     
try:
  words = readFile('input.txt')
  calibrationValues = findCalibrationValue(words)
  print(calculateCalibrationSum(calibrationValues))
except FileNotFoundError as e:
  print(f'Error! File not found. ==> {e}')