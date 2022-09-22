x = [int(input("напечататйте элемент: ")) for i in range(y)]
y = int(input("колво элементов: "))
x.sort()
print("наименьшее число",x[0])
print("индекс наименьшего числа - 0" )
#ex 2 (2)
x = [-1,2,-3,4]
y=[]
z=[]
for i in range (len(x)):
    if x[i] >=0:
        y.append(x[i])
    if x[i]<0:
        z.append(x[i])
print(x)
print(y)
print(z)