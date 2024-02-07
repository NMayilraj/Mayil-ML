import os

def large_arr(large, n):
    ans = max(large)
    return ans;
if __name__ == '__main__':
    large = [10, 20, 30, 40]
    n = len(large)
    print("The large number in the array is", large_arr(large, n))

    



def largest(arr, n):
    ans = max(arr)

    return ans;
 
arr = [10, 324, 45, 90, 9808]
n = len(arr)

print ("Largest in given array ", largest(arr, n))