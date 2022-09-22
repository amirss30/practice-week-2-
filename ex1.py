#ex1 number 1
y = int(input("колво элементов: "))
x = [int(input("напечатайте элемеент: ")) for i in range(y)]
g = 0
for i in range(y):
    if x[i] > g:
        g = x[i]
print("высшее значение",str(g))
x.reverse()
print(x)
#ex1 number 2
x = [int(input("напечатайте элемент: ")) for i in range(y)]
y = int(input("колво элементов: "))
g = 0
sum = 0
f=0
for i in range(y):
    sum += x[i]
    f+=1
for i in range(y):
    if x[i] == 0:
        x[i] = (sum/f)

print(x)