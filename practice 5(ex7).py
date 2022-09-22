import math
x = str(input("введите текст: "))
y=0
list(x)
for i in range(math.ceil(len(x)/2)):
    if x[i] == "n":
        print(x.replace("n","*"))
        y+=1
print(str(y), "колво замен")