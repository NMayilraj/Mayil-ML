
# Program to add two matrices using nested loop
 
x = [1, 2, 3, [4, 5, 6], 7, 8, [9, 1, 2], 3, 4, 5]
y = []
def single_list(x):  
    for i in x:
        if type(i) is list:
            single_list(i)
        else:
            y.append(i)     
    return y
y = single_list(x)
print(y)

