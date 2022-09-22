words = "i tupoi prosto amir"
word = words.split()
for w in word:
    if w.endswith('i'):
        print(w)
    else:
        if w.startswith('a'):
            print(w)
        pass