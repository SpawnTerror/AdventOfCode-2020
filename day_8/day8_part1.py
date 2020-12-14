# SpawnTerror 2020
# Python 3.9

def input_file():
    with open('day_8/input.txt', 'r') as f:
        data = f.read().splitlines()
        commands = {line_number: [str, int] for line_number in range(0, len(data))}
        counter = 0 
        for line in data:
            command = line.split(' ')[0]
            value = line.split(' ')[1]
            commands[counter] = [command, value]
            counter += 1
    return commands

def evaluate(commands):
    accumulator = 0
    index = 0
    visited = []
    while index not in visited and index != len(commands):
        command = commands[index][0]
        value = commands[index][1]
        visited.append(index)
        if command == 'nop':
            index += 1
        elif command == 'jmp':
            index += int(value)
        elif command == 'acc':
            accumulator += int(value)
            index += 1
    return accumulator, index

def part_1(commands):
    return evaluate(commands)[0]
    
commands = input_file()
print(f'Part 1 {part_1(commands)}')
