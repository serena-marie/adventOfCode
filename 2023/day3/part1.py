from pathlib import Path

isSymbol = lambda char : not char.isdigit() and char != '.'

def readFile(filename):
  file_path = Path(__file__).parent / filename

  with open(file_path, 'r') as file:
    strings = file.read().split('\n')
    lines = [word for word in strings]
    return lines

def isAdjacentSymbol(row_pos, col_pos, lines):
  directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  for dir_row, dir_col in directions:
    new_row, new_col = row_pos + dir_row, col_pos + dir_col
    try:
      adj = lines[new_row][new_col]
      if isSymbol(adj):
        return True
    except IndexError as _:
      continue
  return False
   

try:
  result = []
  lines = readFile('mini_input.txt')
  for i, line in enumerate(lines):
    col_pos = 0
    num = ''
    track_part_num = []
    while col_pos < len(line): # Looping through the line
      if line[col_pos].isdigit(): # If current item is a digit 
        num += line[col_pos] # Start building number
        track_part_num.append(isAdjacentSymbol(i, col_pos, lines)) # See if number has adj symbol, returning true/false
        if True in track_part_num:
          while col_pos + 1 < len(line) and line[col_pos + 1].isdigit():
            num += line[col_pos + 1]
            col_pos += 1  # Move to the next character
          result.append(num)
          num = ''
          track_part_num = []
      else:
        if num:
          num = ''
      col_pos+=1

  part1_total = sum(map(int, result))
  print(part1_total)
      
except FileNotFoundError as e:
  print(f'Error! File not found. ==> {e}')