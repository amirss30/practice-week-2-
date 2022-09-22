y = [5, 56, 4, -55, 7, 28, -85, 1, 14, 87, -15, -22, 3]
odd = 1
even = 0
for i in range(len(y)):
    if y[i] % 2 != 0:
        odd = odd * y[i]
    else:
        even += y[i]
print('сумма четных элементов: ', even)
print('произведение нечетных элементов: ', odd)
#2
y = [5, 56, 4, -55, 7, 28, -85, 1, 14, 87, -15, -22, 3]
m = y.index(max(y))
n = y.index(min(y))
Max = max(y)
Min = min(y)
y[m] = Min
y[n] = Max
print(y)