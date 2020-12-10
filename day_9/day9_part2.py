from itertools import permutations

sort = [1, 5, 8, 2, 6, 8]
print(sort)
sort_me = set(list(permutations(sort, 2)))
print(sort_me)
sorted_all_possible = set(map(lambda x: tuple(sorted(x)),sort_me))
print(sorted_all_possible)
sorted_all_possible2 = set(map(lambda x: tuple(sorted(x)),sort_me))
print(sorted_all_possible2)