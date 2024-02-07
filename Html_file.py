      
import os
directory = "c:/Users/Mayilraj\Documents\Learning"

file_Name = []
fname = []
for root, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        if filename in filenames:
            fname = os.path.join(filename)
            file_Name.append(fname)
# print(file_Name)                      
           
def create_list(Exp):
    fileCounter = len(file_Name)
    # print(fileCounter)
    Result = "The total number of "+ Exp.replace("*.","") +" files are " + str(fileCounter) + "\nThe files are below\n"
    # print(Result)
    Res = ""
    coumter = 1
    for hf in file_Name:
        if hf.split(".")[-1] == Exp:
            Res = Res + str(coumter) + ". "+ directory + "\\" + hf + '\n'
            coumter += 1

        R1 = Result + str(Res)  
    return R1   
Content = create_list("htm")
print(Content)















