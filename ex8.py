y = [5, 56, 4, -55, 7, 28, -85, 1, 14, 87, -15, -22, 3]
x = 1
z = 0
for i in range(len(y)):
    x = x*y[i]
    z += y[i]
print('продукт массива: ', x)
print('сумма массива: ', z)
#2
import math
n = int(input('введите длину массива: '))
x = []
for i in range(n):
    print('введите элемент: ')
    x.append(int(input()))
print(math.fabs(min(x)))
x.reverse()
print(x)
