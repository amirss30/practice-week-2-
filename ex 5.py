y = int(input("колво элементов: "))
x = [int(input("напечатайте элемент: ")) for i in range(y)]
z=[]
for i in range(y):
    if x[i]<0:
        print(x[i+1])
    if x[i]==len(x) and x[i]< 0:
        print("нет пары рядом")
#2
x = [5, 56, 4, -55, 7, 28, -85, 1, 14, 87, -15, -22, 3]
y = [*set(x)]
print(y)