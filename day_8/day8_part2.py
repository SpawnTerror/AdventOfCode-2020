# SpawnTerror 2020
# python 3.9 

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

def part_2(commands):
    for i in range(len(commands)):
        command = commands[i][0]
        value = commands[i][1]
        if command == "jmp":
            command = 'nop'
            commands[i] = [command, value]
            accumulator, index = evaluate(commands)
            command = 'jmp'
            commands[i] = [command, value]
        elif command == "nop":
            command = 'jmp'
            commands[i] = [command, value]
            accumulator, index = evaluate(commands)
            command = 'nop'
            commands[i] = [command, value]
        if index == len(commands):
            return accumulator

commands = input_file()
print(f'Part 1 {part_1(commands)}')
print(f'Part 2 {part_2(commands)}')