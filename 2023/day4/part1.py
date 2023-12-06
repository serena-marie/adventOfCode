from pathlib import Path
import re

def readFile(filename, directory="input"):
  file_path = Path(__file__).parent / directory / filename

  with open(file_path, "r") as file:
    strings = file.read().split('\n')
    lines = [line for line in strings]
    return lines

def findWinningCards(cards):
  winner_winner = [] # chicken dinner
  win_counts = [] # part_2
  for card in cards:
    # _ to ignore declaring variable when unpacking
    _, winning_numbers_packed, my_numbers_packed = [item.strip() for item in re.split(r": |\|", card)]
    
    winning_numbers = [int(item.strip()) for item in re.split(r"\s+", winning_numbers_packed)]
    my_numbers = [int(item.strip()) for item in re.split(r"\s+", my_numbers_packed)]
    
    intersection = list(set(winning_numbers) & set(my_numbers))
    winner_winner.append(intersection)
    
  return winner_winner

def calculatePoints(winner_winner):
  total_points = 0
  for card in winner_winner:
    if len(card) > 0:
      current_point = 1
    else:
      current_point = 0

    for i in range(len(card)):
      if i > 0:
        current_point += int(2 ** (i - 1))

    total_points += current_point
  return total_points

try:
  lines = readFile('input.txt')
except FileNotFoundError as error:
  print(f'Error! File not found. ==> {error}')

winning_cards = findWinningCards(lines)
print(f'Part 1: {calculatePoints(winning_cards)}')
# 24706