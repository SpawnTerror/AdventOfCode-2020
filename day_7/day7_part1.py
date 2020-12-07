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
