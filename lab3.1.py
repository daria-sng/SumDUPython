word = str(input("Enter a word with at least 4 letters: "))
while (len(word) < 4 or not word.isalpha()):
    word = str(input("At least 4 letters!: "))

print(f"The second and penultimate letter in your word: {word[1:2]} and {word[-2:-1]}")
