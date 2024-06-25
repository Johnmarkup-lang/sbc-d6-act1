word = input("Enter the word: ").replace(" ", "").lower()
palin_word = ""

for char in word:
    palin_word = char + palin_word

if word == palin_word:
    print("Yes,", word, "is a palindrome.")
else:
    print("No,", word, "is not a palindrome.")
