def check_Div(number):
    messages = {2: "two", 3: "three", 4: "four"}
    Mess = "".join(messages[i] for i in messages if number % i == 0)
    return Mess.strip() if Mess else "Zero"
number = int(input("Please enter your number: "))
result = check_Div(number)
print(result)
