# SpawnTerror 2020
# Python 3.9
# AOC Day 9 Part 1

from itertools import combinations

with open('day_9/input.txt', 'r') as f:
    lines = f.read().splitlines()

def part_1(lines, index):
    preamble = []
    valid = []
    for i in range(len(lines) - index):
        check_number = int(lines[i + index])
        preamble = list(lines[i:i + index])
        for numbers in combinations(preamble, 2):
            if int(numbers[0]) + int(numbers[1]) == check_number:
                valid.append(check_number)
    for number in list(lines[index:]):
        if int(number) not in valid:
            return number
                
def part_2(invalid_number):
    numbers = list(map(int, lines))
    for start_position in range(0, (len(numbers)-1)):
        for end_position in range((start_position + 1), (len(numbers))):
            array_of_numbers = numbers[start_position:end_position]
            array_sum = sum(array_of_numbers)
            if int(array_sum) > int(invalid_number):
                break
            elif int(array_sum) == int(invalid_number):
                return min(array_of_numbers) + max(array_of_numbers)

# Part 1's second argument takes any preamble number
# for example: part_1(lines, 5) for testing with sample.txt as input

invalid_number = part_1(lines, 25)
print(f'Part 1: {invalid_number}.')
print(f'Part 2: {part_2(invalid_number)}.')
