def square(n):
    n=[]
    if n == 0:
        return 1
    else:
        return n * n

# Test the function
number = 22
result = square(number)
print("The square of {} is: {}".format(number, result))