import random
for i in range(0,11):
    print(str(i).zfill(3))


#way 2
num=random.randint(0,99)
print("way-2:",f'{i:03d}')


#way 3

addzero=lambda number,zeros:"{0:0{1}d}".format(number,zeros)

print("way-3:",addzero(2,3))


