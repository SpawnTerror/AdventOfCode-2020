# ADvent Of Code
# Day 5 Part 1
# SpawnTerror 2020

with open('day_5/input.txt', 'r') as f:

    boarding_passes = [line for line in f.read().splitlines()]

def validate_data(data):

    list_of_ids = []

    for address in boarding_passes:     

        rows = [row for row in range (0, 128)]
        columns = [column for column in range (0, 8)]
        
        for letter in address[:7]:
            if len(rows) != 1:
                if letter == 'F':
                    rows = rows[:len(rows)//2]   
                elif letter =='B':
                    rows = rows[len(rows)//2:]
                
        for letter in address[7:]:
            if len(columns) != 1:
                if letter == 'L':
                    columns = columns[:len(columns)//2]
                elif letter == 'R':
                    columns = columns[len(columns)//2:]

        seat_id = (int(rows[0]) * 8 + int(columns[0]))
        list_of_ids.append(seat_id)
        
    print(f'Highest seat ID found in the list: {max(list_of_ids)}')
    
if __name__ == '__main__':

    validate_data(boarding_passes)