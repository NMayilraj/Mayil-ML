Name = ["Suriya","pradeep","john"]
Age = ["28","38","48"]
City = ["Chennai", "Salem", "Madurai"]

def details(NM, AG, CT):
    Result = "My name is {0}, and my age is {1}, and i am from {2}".format(NM, AG, CT)
    print(Result)

for i in range(len(Age)):

    NM=Name[i]
    AG=Age[i]
    CT=City[i]
    details(NM, AG, CT)


