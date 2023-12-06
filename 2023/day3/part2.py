from pathlib import Path
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

isSymbol = lambda char : not char.isdigit() and char != '.'
isGearSymbol = lambda char : char == '*'

def readFile(filename):
  file_path = Path(__file__).parent / filename

  with open(file_path, 'r') as file:
    strings = file.read().split('\n')
    lines = [word for word in strings]
    return lines


directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
gears = {}
res = 0

try:
  result = []
  lines = readFile('input.txt')
  for row, line in enumerate(lines):
    num = 0
    gear = False
    for col, char in enumerate(line):
      if char.isdigit():
        num = num * 10 + int(lines[row][col]) # witchcraft provided by Taylor
        print(num)
        for dir_row, dir_col in directions:
          new_row, new_col = dir_row + row, dir_col + col
          if(new_row < 0 or new_col < 0): # -1 is a valid index so IndexError isn't thrown
            continue
          try:
            adj = lines[new_row][new_col]
            if isGearSymbol(adj):
              gear = (new_row, new_col)
          except IndexError:
            continue
      if not char.isdigit() or col == len(line) - 1:
        if gear:
          gears.setdefault(gear, []).append(num)
          if len(gears[gear]) == 2:
            res += num*int(gears[gear][0])
          gear = False
        num = 0    
  print(res)     
except FileNotFoundError as e:
  print(f'Error! File not found. ==> {e}')
  
# 76314915