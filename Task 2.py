import os
import glob
path = "c:/Users/Mayilraj\Documents\Learning"
fname = []

for root, d_names, f_names in os.walk(path):
    for f in f_names:
        fname.append(os.path.join(f))
print(fname)
            
# def create_list(fname):         
#     file_Name = glob.glob1(path,fname)
#     fileCounter = len(file_Name)
#     Result = "The total number of "+ fname.replace("*.","") +" files are " + str(fileCounter) + "\nThe files are below\n"
#     Res = ""
#     coumter = 1
#     for hf in file_Name:
#         Res = Res + str(coumter) + ". "+ path + "\\" + hf + '\n'
#         coumter += 1
#         R1 = Result + str(Res)
#         return R1

# Content = create_list("*.html") + "\n" + create_list("*.pdf") + "\n" + create_list("*.zip") + "\n" + create_list("*.htm") + "\n" + create_list("*.txt") + "\n" + create_list("*.py")
# print(Content)

# def wr():
#     file = open("myfiles.txt","w")
#     file.write(Content)
#     file.close()