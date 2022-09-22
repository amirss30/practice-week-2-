x = str(input("введите текст: "))
print(x.split(' '))
y=0
if x[0]=='е':
    y+=1
for i in range(len(x)-1):
    if x[i] == ' ':
        if x[i+1]=='е':
            y+=1
    i+=1
print(str(y), " - число слов начинающиеся на букву 'e'")