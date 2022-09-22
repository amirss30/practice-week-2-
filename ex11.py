y = [5, 56, 4, -55, 7, 28, -85, 1, 14, 87, -15, -22, 3]
x = []
for i in range(len(y)):
    if y[i] % 2 == 0:
        x.append(y[i])
print(max(x))
#2
y = [5, 56, 4, -55, 7, 28, -85, 1, 14, 87, -15, -22, 3]
x = []
for i in range(len(y)):
    if y[i] < 10 and y[i] % 2 == 0:
        x.append(y[i])
x.reverse()
if len(x) == 0:
    print('таких элементов нет.')
else:
    print(x)
    