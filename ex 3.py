n = int(input("колво элементов: "))
t = [int(input("напечатайте элемент: ")) for i in range(n)]
sum = 0
for i in range(n):
    if t.index(t[i], 0, len(t)) % 2 == 0:
        sum += t[i]
print("сумма нечетных элементов", str(sum))
print(t)
print("колво элементов", str(len(t)))
#2
x = [int(input("напечатайте элемент: ")) for i in range(8)]
for i in range(8):
    if x[i] < 15:
        x[i] = x[i] * 2
print(x)