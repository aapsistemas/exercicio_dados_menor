import random

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)

print(f'd1: {d1}')
print(f'd2: {d2}')

if d1 < d2:
    print('O valor do dado 1 é, ' + str(d1) + ', que é menor que d2')

elif d1 == d2:
    print('os dados tem o mesmo valor')

else:
    print('O valor do dado 2 é, ' + str(d2) + ', que é menor que d1')
