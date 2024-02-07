Number = int(input("Please Enter the Number: "))

List = [2, 3, 4]
Output = ["Two", "Three", "Four"]
Final = []
for i in List:
    if Number % i == 0:  
        position = List.index(i)
        New = Output[position]
        Final.append(New)
    if Number % i != 0:
        print("Zero")
       
print(Final)