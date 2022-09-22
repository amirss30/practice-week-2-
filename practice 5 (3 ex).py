x = str(input("введите текст: "))
print(list(x))
y=0
for i in range(len(x)):
    if x[i] == '.':
        x.replace('.','')
        y+=1
print(str(y), " колво замен")
