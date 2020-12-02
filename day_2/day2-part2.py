import re

entries = []
line_counter = 0
correct_pass_count = 0

with open('day_2/input_list.txt', 'r') as f:
    for line in f:
        entries.append(line)

for entry in entries:
    linet = entries[line_counter]
    found_letters_count = 0

    split_linet = re.findall(r"[\w']+", linet)
    x1 = int(split_linet[0]) 
    x2 = int(split_linet[1]) 
    target_letter = str(split_linet[2])
    password = str(split_linet[3])

    # Enumerate function 'positions' starts from 0 down below, x1 and x2 needs to be shifted -1 to accomodate for it
    x1 -= 1
    x2 -= 1

    positions = []
    positions = [pos for pos, char in enumerate(password) if char == target_letter]
 
    positives = 0
    for position in positions:

        if int(position) == x1:
            positives += 1
        if int(position) == x2:
            positives += 1

    if positives == 1:
        correct_pass_count += 1

    line_counter += 1  

print(f'Found {correct_pass_count} correct password(s) matching the policy.')


























'''
import re

entries = []
m = 0
x1 = 0
x2 = 0

with open('day_2/input_list.txt', 'r') as f:
    for line in f:
        entries.append(line)

linet = entries[4]

extracted_floats = [float(s) for s in re.findall(r'-?\d+\.?\d*', linet)]
x1 = abs(int(extracted_floats[0]))
x2 = abs(int(extracted_floats[1]))
print(x1, x2)
print(linet.split(':')[0])
'''