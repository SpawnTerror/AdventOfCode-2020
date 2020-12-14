with open('day_10/sample.txt', 'r') as f:
    data = [int(line) for line in f.read().splitlines()]
    adapters = sorted(data)

collected = []

for x in range(0, len(adapters)):
    
    a = int(adapters[x])
    c = int(collected[x])

    if a < c:
        x +=1
    collected.append(adapters)
