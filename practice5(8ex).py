x = str(input("введите текст: "))
y=0
list(x)
for i in range(len(x)):
    if x[i] == " ":
        y+=1
print(str(y+1), "колво слов")