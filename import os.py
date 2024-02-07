import os
import glob
 
# Get the list of all files and directories
path = "C:\\Users\\Mayilraj\\Documents\\Learning\\Search"
dir_list = os.listdir(path)
# print(dir_list)

def create_list(Exp):
    file_Name = glob.glob1(path,Exp)
    fileCounter = len(file_Name)
    Result = "The total number of "+ Exp.replace("*.","") +" files are " + str(fileCounter) + "\nThe files are below\n"
    Res = ""
    coumter = 1
    for hf in file_Name:
        Res = Res + str(coumter) + ". "+ hf + '\n'
        coumter += 1
    R1 = Result + str(Res)
    return R1


Content = create_list("*.html") + create_list("*.pdf") + create_list("*.zip") + create_list("*.htm")
print(Content)


file = open("myfiles.txt","w")
file.write(Content)
file.close()