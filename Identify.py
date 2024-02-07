import re
regex = '^[0-9]+$'
string = input("Please enter your wish: ")

def check(string):
    print(re.search(regex, string))
    if re.search(regex, string) != None:
        print("Digit")     
    else:
        print("Not a Digit")

check(string)
if True:
    print("dd")
else:
    print("false")

# if __name__ == '__main__' :
#     string = "28"
#     check(string)
#     string = "a"
#     check(string)
#     string = "21ab"
#     check(string)
#     string = "12ab12"
#     check(string)