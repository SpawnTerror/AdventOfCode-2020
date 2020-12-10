# 731031916
# 93396727

from itertools import permutations

with open('day_9/input.txt', 'r') as f:
    data = [line for line in f.read().splitlines()]

def day9_part1(preamble):

    decode = int(preamble)

    for number in range(decode, len(data)):
        xmas = int(number)

        list_of_25 = []
        found_pairs = 0

        for e in range(xmas-25, xmas):
            list_of_25.append(data[e])
        
        sort_me = set(list(permutations(list_of_25, 2)))
        sorted_all_possible = set(map(lambda x: tuple(sorted(x)),sort_me))
        
        for i in sorted_all_possible:
            n1, n2, nTest = int(i[0]), int(i[1]), int(data[xmas])

            if n1 + n2 == nTest:
                found_pairs += 1

        if found_pairs == 0:
            break

    return nTest

print(day9_part1(25))
