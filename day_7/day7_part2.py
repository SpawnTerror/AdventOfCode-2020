''' Reminder

shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
Consider again your shiny gold bag and the rules from the above 
example:

- faded blue bags contain 0 other bags.
- dotted black bags contain 0 other bags.
- vibrant plum bags contain 11 other bags: 
  5 faded blue bags and 6 dotted black bags.
- dark olive bags contain 7 other bags: 
  3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 
1 dark olive bag (and the 7 bags within it) 
plus 2 vibrant plum bags (and the 11 bags within each of those): 

1 + 1*7 + 2 + 2*11 = 32 bags!

'''

with open('day_7/input.txt', 'r') as f:
  data = f.readlines()

inventory_bags = {}

for line in data:

  everyline = line.strip("\n").split(sep=" bags contain ")
  main_bag = everyline[0]
  inside_main_bag = []
  bags_in_main_bag = everyline[1].split(sep=", ")
  for each_bag in bags_in_main_bag:
    description = each_bag.split(' bag')[0]
    number_of_bags = description[0]
    type_of_bags = description[2:]
    if number_of_bags == 'n':
      pass # skip 'no other'
    else:
      inside_main_bag.append((type_of_bags, int(number_of_bags)))
  inventory_bags[main_bag] = inside_main_bag


my_bag = ['shiny gold']
loop = True

while loop:
  loop = False
  
  for items in inventory_bags:
    for each_item in inventory_bags[items]:
      if each_item[0] in my_bag and items not in my_bag:
        my_bag.append(items)
  
        loop = True
        break

x = len(my_bag) - 1
print(f'Total bags: {x}')

bags_count_dict = {}

def multiply_content(bag):

    bags_count = 0

    # experimental
    for each in inventory_bags[bag]:
        bags_count += each[1] + each[1] * multiply_content(each[0])

    bags_count_dict[bag] = bags_count
    print(bags_count_dict)
    return bags_count

x = multiply_content('shiny gold')
print(f'Total: {x}')