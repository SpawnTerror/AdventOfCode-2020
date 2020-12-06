import re

rules = {
    'byr': (lambda x: True if int(x) >= 1920 and int(x) <= 2002 else False),
    'iyr': (lambda x: True if int(x) >= 2010 and int(x) <= 2020 else False), 
    'eyr': (lambda x: True if int(x) >= 2020 and int(x) <= 2030 else False), 
    'hgt': (lambda x: True if ("cm" in x and int(x[:x.find("cm")]) >= 150 and int(x[:x.find("cm")]) <= 193) or ("in" in x and int(x[:x.find("in")]) >= 59 and int(x[:x.find("in")]) <= 76) else False),
    'hcl': (lambda x: True if len(x) == 7 and re.match("^#([a-f0-9]{6})", x) else False),  
    'ecl': (lambda x: True if x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else False), 
    'pid': (lambda x: True if len(x) == 9 and int(x) else False)
}
validated = 0
with open("day_4/input.txt", 'r') as f:
    line = f.read().split('\n\n')
    for data in line:
        if data != "":
            text = data.split()
            passport = dict()
            for field in text:
                k, v = field.split(":")
                passport[k] = v
            checks = {key: rules[key](value) for key, value in passport.items() if key in ['byr', 'iyr', 'eyr', 'hcl', 'hgt', 'ecl', 'pid']}
            if all([field in passport.keys() for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]) and all(checks.values()):
                validated += 1
print(f'Valid passports: {validated}')