import string

with open('day_6/input.txt', 'r') as f:
    dirty_data = f.read().split('\n\n')
    dirty_data = [word.replace('\n', '') for word in dirty_data]

dataset = dict.fromkeys(string.ascii_lowercase, 0)
total_valid = 0

for everyline in dirty_data: 
    for ch in everyline:      
        if dataset[ch] == 0:
            dataset[ch] = 1
            
    valid_answer_count = sum(value == 1 for value in dataset.values())
    total_valid += valid_answer_count
    dataset = dict.fromkeys(string.ascii_lowercase, 0)

print(f'\nTotal valid answers: {total_valid}')


