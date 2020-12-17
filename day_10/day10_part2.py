# SpawnTerror 2020
# Python 3.9
# AOC Day 10 Part 2

from collections import Counter

def get_input(input: int) -> list:
    if input == 1: path = 'day_10/sample.txt'
    if input == 2: path = 'day_10/input.txt'
    with open(path, 'r') as file:
        data = [int(number) for number in file.read().splitlines()]
    return data

def part_1(data: list) -> int:
    outlet = 0
    adapters_list = list(sorted(data))
    valid = []
    dif_1j = 0
    dif_3j = 1 
    for i in adapters_list:
        if (i - outlet) <= 3:
            valid.append(int(i))
            if (i-outlet) == 1: dif_1j += 1
            if (i-outlet) == 3: dif_3j += 1
            outlet = i
    return dif_1j * dif_3j

def part_2(data: list) -> int:
    adapters_list = list(sorted(data))
    adapters_list.append(adapters_list[-1] + 3)
    count = Counter()
    count[0] = 1
    for adapter in adapters_list:
        count[adapter] = count[adapter - 1] + count[adapter - 2] + count[adapter - 3]
    return count[adapters_list[-1]]

data = get_input(2)
print(f'Part 1: {part_1(data)}.')
print(f'Part 2: {part_2(data)}.')