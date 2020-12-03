print('\n*** Starting *** \n')

matrix = []
trees = 0
x = 0
factor_x = 0

with open('day_3/input.txt', 'r') as f:
    for line in f:
        matrix.append(line)

last = len(matrix)

for line_number in range(0, last, 1):
    
    string = matrix[line_number].strip()
    string_lenght = len(string)
 
    if (string_lenght - 1) <= factor_x:
        while string_lenght <= factor_x:
            string = string + string
            string_lenght = len(string)
           
    if string[factor_x] == '#':
        trees += 1

    factor_x += 1

print(f'Trees found with coordinates (3, 1): {trees}\n')
