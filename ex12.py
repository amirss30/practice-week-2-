y = [5, 56, 4, -55, 7, 28, -85, 1, 14, 87, -15, -22, 3]
x = []
for i in range(len(y)):
    if y[i] < 10 and y[i] % 2 != 0:
        x.append(y[i])
print(min(x))
#2
y = [5, 56, 4, -55, 7, 28, -85, 1, 14, 87, -15, -22, 3]
x = 1
z = 0
for i in range(len(y)):
    x = x*y[i]
    z += y[i]
print('продукт массива: ', x)
print('сумма массива: ', z)