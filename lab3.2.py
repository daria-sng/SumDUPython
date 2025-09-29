word = str(input("Enter a word: "))
i = 1
while i < len(word):
    if word.count(word[i]) != 1:
        word = word[:i] + word[i+1:]
    else:
        i+=1
print("Result:", word)
