multiples = 0

for i in range(101):
    
    if i % 7 == 0 and i != 0:
        multiples +=1

print(f"Multiples with only one range param: {multiples}")

multiples = 0
for i in range(1, 101, 1):
    if i % 7 == 0: multiples += 1

print(f"Multiples with tree range params: {multiples}")




