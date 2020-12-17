# SpawnTerror 2020
# Python 3.9
# AOC Day 10 Part 1

def get_input(input: int) -> list:
    if input == 1: path = 'day_10/sample.txt'
    if input == 2: path = 'day_10/input.txt'
    with open(path, 'r') as file:
        data = [int(number) for number in file.read().splitlines()]
    return data

def part_1(data: list) -> list:
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

data = get_input(2)
print(f'Part 1: {part_1(data)}.')
