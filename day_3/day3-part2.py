import math

print('\n*** Starting *** \n')

matrix = []
trees = 0
factor_x = 0
results = []
coor = [(1,1),(3,1),(5,1),(7,1),(1,2)]
#coor = [(1,1)]

with open('day_3/input.txt', 'r') as f:
    for line in f:
        matrix.append(line)
last = len(matrix)

for r in range(0, len(coor)):
    shift_x, shift_y = coor[r]
    
    for line_number in range(0, last, shift_y):
        string = matrix[line_number].strip()
        string_lenght = len(string)
        if string_lenght <= factor_x:
            while (string_lenght -1) <= factor_x:
                string = string + string
                string_lenght = len(string)
        if string[factor_x]== '#':
            trees += 1     
        factor_x += shift_x

    results.append(trees)
    trees = 0
    factor_x = 0
    
print(f'Trees found with coordinates {coor[1]}: {results[1]}')
print(f'Trees found with all coordinates {coor}: {results}')
print(f'Multiplying all trees from all runs: {math.prod(results)}\n')
