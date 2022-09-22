x = str(input("введите текст: "))
y=0
list(x)
for i in range(len(x)):
    if x[i] == "a":
        print(x.replace("a",""))
        y+=1
print(str(y), " колво замен")