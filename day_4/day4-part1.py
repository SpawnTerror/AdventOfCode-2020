
input_data = []
document = {}
valid_passports = 0

with open('day_4/input.txt', 'r') as f:
    for everyline in f:
        input_data.append(everyline.strip())

to_check = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) # set

for everyline in input_data:
    if not everyline:
        if to_check.issubset(set(document.keys())):
            valid_passports += 1
        document = {}
    else:
        for dict_pair in everyline.split(' '):
            print(dict_pair)
            k, v = dict_pair.split(':')
            document[k] = v

print(valid_passports)
