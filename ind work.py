#1
a=[5, 8, 4, 7, 3, 2]
a.reverse()
print(a)
#2
a=[10, 5]
a[0], a[-1]=a[-1], a[0]
print(a)
#3
a= [5, 8, 4, 7, 3, 2]
for i in a:
    print(i, end=' ')
#4
a= [150, 200, 100, 90, 140, 110]
Ln=a[0]
for number in a:
    if number>Ln:
        Ln=number
b=len(a)
print(Ln/b)
#5
a= [15, 52, 14, 87, 10, 148]
a.sort(reverse=True)
print(a)