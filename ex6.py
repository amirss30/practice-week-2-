y = [5, 56, 4, -55, 7, 28, -85, 1, 14, 87, -15, -22, 3]
less = 0
greater = 0
print('максимум массива: ', max(y))
for i in range(len(y)):
    if y[i] < max(y):
        if y[i] > y[i-1]:
            less = y[i]
        else:
            less = y[i-1]
    else:
        if (y[i] > y[i-1]):
            greater = y[i]
            if y[i] == max(y):
                print('нет элемента больше максимального')
        else:
            greater = y[i-1]
            if y[i-1] == max(y):
                print('Нет элемента больше максимального')
print('элемент меньше максимума: ', less)
#2
x = []
n = 10
sum = 0
for i in range(n):
    x.append(int(input('введите элементы массива: ')))
for i in range(n):
    if x[i] > 5:
        sum += x[i]
print(sum)
