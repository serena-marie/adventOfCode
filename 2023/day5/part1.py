from pathlib import Path
import re

# mapping = [['seed','soil'], ['soil', 'fert'], ['fert', 'water'], ['water','light'], ['light', 'temp'], ['temp', 'humidity'], ['humidity', 'location']]

def readFile(filename, directory="input"):
  file_path = Path(__file__).parent / directory / filename

  with open(file_path, "r") as file:
    strings = file.read().split('\n')
    lines = [line for line in strings]
    return lines

def parseData(data):
  # Remove empty new lines
  lines = list(filter(lambda x: x.strip() != "", data))

  seeds_line = [item.strip() for item in re.split(r":\s+|\s+", data[0])]

  seeds_list = seeds_line[1:]
  maps = lines[2:]
  return seeds_list, maps


try:
  lines = readFile('mini_input.txt')
except FileNotFoundError as e:
  print(f'Error! {e}')

seeds_list, maps = parseData(lines)

locations = []
for seed in seeds_list:
  mapping_found = False
  for i, line in enumerate(maps):
    if 'map' in line:
      mapping_found = False
      continue

    seed = int(seed)
    dest_start, src_start, range_len = map(int, line.split(" "))

    if not mapping_found and src_start <= seed < src_start + range_len:
      gap = dest_start-src_start
      seed = seed + gap
      mapping_found = True

  locations.append(seed)

min_location = locations[0]
for location_num in locations[1:]:
  min_location = min(min_location, location_num)
print(f'Min location {min_location}') # 51752125
