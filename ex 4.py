y = int(input("колво элементов: "))
x = [int(input("напечатайте элемент: ")) for i in range(y)]
z = 0
for i in range(y):
    if x[i] > z:
        z = x[i]
print("наибольшее число",str(z))
print(str(x.index(z,0,len(x)))," - порядковый номер")
# 2
y = int(input("колво элементов: "))
x = [int(input("напечатайте элемент: ")) for i in range(y)]
z=[]
for i in range(y):
    if x[i]%2==0:
        z.append(x[i])
z.sort()
print(z)
