x = str(input("введите текст: "))
y=0
list(x)
for i in range(len(x)):
    if x[i] == "a":
        x.replace("a","o")
        y+=1
print(str(y), "колво замен")
print(len(x.replace(' ', '')), "колво символов")