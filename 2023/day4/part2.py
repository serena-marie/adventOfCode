from pathlib import Path
import re

def readFile(filename):
  file_path = Path(__file__).parent / filename

  with open(file_path, "r") as file:
    strings = file.read().split('\n')
    lines = [line for line in strings]
    return lines

def find_winning_cards(cards):
  winner_winner = [] # chicken dinner
  for card in cards:
    # _ to ignore declaring variable when unpacking
    _, winning_numbers_packed, my_numbers_packed = [item.strip() for item in re.split(r": |\|", card)]
    winning_numbers = [int(item.strip()) for item in re.split(r"\s+", winning_numbers_packed)]
    my_numbers = [int(item.strip()) for item in re.split(r"\s+", my_numbers_packed)]
    
    # Find the intersection of the two lists and append
    winner_winner.append(list(set(winning_numbers) & set(my_numbers)))   
  return winner_winner

def add_copies(num_of_wins, copies, current_round):
  next_round = current_round+1
  for _ in range(num_of_wins):
    # start at next_round to increment each by copies in current round
    if next_round < len(copies):
      copies[next_round]+=copies[current_round]
      next_round+=1
  return copies

def process_scratchcards(winner_winner):
  win_counts = [len(item) for item in winner_winner] # reference of number of wins for each card
  process_copies = [1 for _ in range(len(win_counts))] # process_copies = [[] * buckets] # not like thiiis
  for game_number in range(len(process_copies)):
    game_copy = 0
    if process_copies[game_number] > 0:
      # look up number of wins
      this_games_wins = win_counts[game_number]
      # Now add copies to process_copies
      add_copies(this_games_wins, process_copies, game_number)        
    game_copy+=1
  return process_copies

def calc_scratchcard_num(scratchcard_list):
  total_sum = 0
  for card in scratchcard_list:
    total_sum+=card
  return total_sum

try:
  lines = readFile('input.txt')
except FileNotFoundError as error:
  print(f'Error! File not found. ==> {error}')

winning_cards = find_winning_cards(lines)
processed = process_scratchcards(winning_cards)
print(f'Part 2: {calc_scratchcard_num(processed)}')