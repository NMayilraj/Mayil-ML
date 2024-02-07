Low = 1
high = 1000
print("Please think of a number between {} and {}".format(Low, high))

guesses = 1

while True:
    print("\tGuessing in the range of {} and {}".format(Low, high))
    guess = Low + (high - Low) // 2
    High_Low = input("My guess is {}. Should i guess high or low?. Please enter H or L or C if my guess is correct ".format(guess))
    if High_Low == "H":
        Low = guess - 1
    elif High_Low == "L":
        high = guess + 1
    elif High_Low == "C":
        print("Kumaran, I guessed it correctly in {} guesses.".format(guesses))
        break
    else:
        print("Please enter H or L or C")
    guesses = guesses + 1

    