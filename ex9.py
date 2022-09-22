import math
n = int(input('введите длину массива: '))
x = []
for i in range(n):
    print('введите элемент: ')
    x.append(int(input()))
print(math.fabs(min(x)))
x.reverse()
print(x)