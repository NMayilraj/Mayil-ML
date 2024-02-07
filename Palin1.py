Word = input("Please enter your text: ")
rev = Word[::-1]
if Word == rev:
    print("The given text is palindrome")
else:
    print("The text is not palindrome")
