import itertools 


entries = []
with open('day_1/input_list.txt', 'r') as f:
    for line in f:
        entries.append(int(line))

target = 2020

for numbers in itertools.combinations(entries,3):
    if sum(numbers) == target:
        print(numbers)
        number_1 = int(numbers[0])
        print(number_1)
        number_2 = int(numbers[1])
        print(number_2)
        print(f'Result = {number_1 * number_2}')


