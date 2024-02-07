def is_palindrom(string):
    return string[::-1].casefold() == string.casefold()

word = input("Please enter a word to check if it is palindrom: ")
# New = word.casefold()

if is_palindrom(word):
    print("The word {} is palindrome".format(word))
else:
    print("The word {} is not a palindrome".format(word))


