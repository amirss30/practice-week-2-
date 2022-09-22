x = str(input("введите текст: "))
n = str(input("данное слово: "))
y = 0
x = x.split(" ")
for i in range(len(x)):
    if x[i] == n:
        y += 1
print(str(y), "колво повторений")