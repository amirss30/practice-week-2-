x = []
n = 10
y = []
for i in range(n):
    x.append(int(input('введите элементы массива(10): ')))
for i in range(n):
    if x[i] == x[i-1]:
        y.append(x[i])
if len(y) == 0:
    print('нет повторяющихся элементов.')
else:
    print('повторяющиеся элементы: ', y)