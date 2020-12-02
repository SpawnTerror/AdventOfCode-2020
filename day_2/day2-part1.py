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

    for character in password:
        if character == target_letter:
            found_letters_count += 1           
    if x1 <= found_letters_count <= x2:
        correct_pass_count += 1
    line_counter += 1   

print(f'Found {correct_pass_count} correct password(s) matching the policy.')
