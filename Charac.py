Input = input("Please enter you wish: ")

def check(string):
    try:
        float(string)
        print("Numeric")
    except ValueError:
        print("It is a text")

check(Input)
