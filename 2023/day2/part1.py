#####################################
# Doesn't work
#####################################
from pathlib import Path
import re
RED_CUBES_TOTAL = 12
GREEN_CUBES_TOTAL = 13
BLUE_CUBES_TOTAL = 14
TOTAL_CUBES = RED_CUBES_TOTAL + GREEN_CUBES_TOTAL + BLUE_CUBES_TOTAL

def testFunction():
  pass

def readFile(filename):
  file_path = Path(__file__).parent / filename

  with open(file_path, "r") as file:
    strings = file.read().split('\n')
    lines = [line for line in strings]
    return lines

def getGameSets(list_of_games):
  game_sets = []
  for game in list_of_games:
    # https://stackoverflow.com/a/4071407
    current_set = [item.strip() for item in re.split(r":|;", game)]
    game_sets.append(current_set)
  return game_sets

def seperateSetsByColor(list_of_sets):
  game_set_list = []
  for game_set in list_of_sets:
    level = []
    for data_in_set in game_set:
      split_by_color = [item.strip() for item in re.split(',', data_in_set )]
      level.append(split_by_color)
    game_set_list.append(level)
  # print(game_set_list)
  return game_set_list

def organize_game_set_data(separated_sets):
  organized_set_of_games = []
  for game_set in separated_sets: # [['Game 1'], ['1 red', '3 blue', '11 green'], ['1 blue', '5 red'], ['3 blue', '5 green', '13 red'], ['6 red', '1 blue', '4 green'], ['16 red', '12 green']]
    level = []
    for set_element in game_set:
      current = set_element.pop()
      if 'Game' in current:
        continue
      print('im inside set_element', set_element)
    print('im outside set_element', current)

  # for game_set in separated_sets:
  #   set_data = []
  #   set_results = {'red': 0, 'blue': 0, 'green': 0}
  #   print(game_set)
  #   for set_element in game_set:
  #     current = set_element[0]
  #     if 'Game' in current:
  #       continue
  #     print(current)

  #     split_indv_color = [item.strip() for item in current.split()]
  #     value, color = split_indv_color
  #     if color in set_results:
  #       set_results[color] += int(value)
  #     else:
  #       print(f'Unexpected color! Received {color}')

  #   # set_data.append(set_results.copy())  # Append a copy of the set_results dictionary
  #   # organized_set_of_games.append(set_data)

  return organized_set_of_games
def outOfRange(value, color):
  if color == 'red':
    return RED_CUBES_TOTAL < value
  if color == 'green':
    return GREEN_CUBES_TOTAL < value
  if color == 'blue':
    return BLUE_CUBES_TOTAL < value

def isGamePossible(game_results):
  results = []
  for results in game_results:
    pass
    # print(f'results {results}')
  # results = []
  # for idx, game_set in enumerate(game_results):
  #   print('evaluating ', game_set)
  #   total = 0
  #   false_flag = False
  #   for key, value in game_set.items():
  #     print(f'{key}: {value}')
  #     if outOfRange(value, key):
  #       results.append(False)
  #       false_flag = True
  #       print('value out of range, I want to exit loop to next set\n\n')
  #       break
  #   if(not false_flag):
  #     print('we made it to the end, value is true\n')
  #     results.append(True)
  # return results

def calculateSumOfGames(boolean_results):
  total_sum = 0
  for idx, result in enumerate(boolean_results):
    if(result):
      total_sum += idx + 1
  return total_sum



try:
  games = readFile('input/input.txt')
  game_sets = getGameSets(games)
  separated_sets = seperateSetsByColor(game_sets)
  list_of_game_results = organize_game_set_data(separated_sets)
  print(list_of_game_results)
  is_game_possible_results = isGamePossible(list_of_game_results)
  # print(is_game_possible_results)
  # sum_of_games = calculateSumOfGames(is_game_possible_results)
  # print(sum_of_games)
except FileNotFoundError as error:
  print(f'Error! File not found. ==> {error}')