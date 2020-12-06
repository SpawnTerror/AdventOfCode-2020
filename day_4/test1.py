required_fields=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
 
def byr_val(value):
    if len(value) != 4:
        return False
    value = int(value)
    if value >= 1920 and value <= 2002:
        return True
    return False
 
def iyr_val(value):
    if len(value) != 4:
        return False
    value = int(value)
    if value >= 2010 and value <= 2020:
        return True
    return False
 
def eyr_val(value):
    if len(value) != 4:
        return False
    value = int(value)
    if value >= 2020 and value <= 2030:
        return True
    return False
 
def hgt_val(value):
    try:
        num, end = int(value[:-2]), value[-2:]
    except ValueError:
        return False
    if end in ['cm', 'in']:
        if end == 'cm':
            if num >=150 and num<= 193:
                return True
        else:
            if num >=59 and num<= 76:
                return True
    return False
 
def hcl_val(value):
    if len(value) != 7:
        return False
    prefix, value = value[0], value[1:]
    if prefix == '#':
        for digit in value:
            if digit not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                return False
    return True
 
def pid_val(value):
    if len(value) != 9:
        return False
    try:
        value = int(value)
    except BaseException:
        return False
    return True
 
def ecl_val(value):
    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False
 
 
validators= {'byr':byr_val, 'iyr':iyr_val, 'eyr':eyr_val, 'hgt':hgt_val, 'hcl':hcl_val, 'ecl':ecl_val, 'pid':pid_val}
valid_passpords = 0
 
with open("day_4/input.txt", 'r') as f:
    current_fields = {}
    for line in f.readlines():
        if len(line) != 1:
            fields = line.split()
            for data in fields:
                key, value = data.split(":")
                if validators.get(key, lambda x: True)(value):
                    current_fields[key]=value
                else:
                    break
        else:
            for rf in required_fields:
                if rf not in current_fields.keys():
                    break
            else:
                valid_passpords += 1
            current_fields = {}
 
print(valid_passpords)