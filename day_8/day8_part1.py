#Part 1: 1553
#Part 2: 1877

def get_file(name):
    with open(name, 'r') as f:
        data = f.read().split(sep='\n')
    return data

def process_commands(data):
    commands = {line_number: [str, int, False] for line_number in range(0, len(data))} 
    line_counter = 0

    for line in data:
        command = line.split(' ')[0]
        parameter = line.split(' ')[1]
        commands[line_counter] = [command, parameter, False]
        line_counter += 1  
    return commands

def execute(command):
    position = 0
    add_value_to_acc = 0

    if command[0] == 'nop':
        pass
    elif command[0] == 'acc':
        add_value_to_acc += int(command[1])
    elif command[0] == 'jmp':
        position += int(command[1])
        
    return [add_value_to_acc, position]

def run(commands):
    accumulator = 0
    c = 0
    
    while True:
        command = commands[c]
        
        if command[2] == False:
            commands[c] = [command[0], command[1], True]
            returned = execute(command)
            accumulator += returned[0]
        else:  
            
            break   
        if returned[1] == 0:
            c += 1
        else:       
            c += int(returned[1])
            
    return accumulator

data = get_file('day_8/input.txt')
commands = process_commands(data)

print(f'\n*** Accumulator value ---- {run(commands)}.')