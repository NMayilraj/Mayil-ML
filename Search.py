# import OS module
import os
import glob
 
# Get the list of all files and directories
path = "C:\\Users\\Mayilraj\\Documents\\Learning\\Search"
dir_list = os.listdir(path)
# print(dir_list)

htmfile_Name = glob.glob1(path,"*.htm")
htmlfile_Name = glob.glob1(path,"*.html")
pdffile_Name = glob.glob1(path,"*.pdf")
zipfile_Name = glob.glob1(path,"*.zip")  

htmCounter = len(htmfile_Name)
htmlCounter = len(htmlfile_Name)
pdfCounter = len(pdffile_Name)
zipCounter = len(zipfile_Name)
files = [htmfile_Name, htmlfile_Name, pdffile_Name, zipfile_Name]
Result = "The total number of htm files are " + str(htmCounter) + "\nThe files are below\n"
def create_list(files):
    Res = ""
    coumter = 1
    for hf in htmfile_Name:
        Res = Res + str(coumter) + ". "+ hf + '\n'
        coumter += 1
    R1 = Result + str(Res)
    print(R1)
create_list(files)
print(create_list(files))
  
# file = open("myfiles.txt","w")
# file.write(str(R1))
# file.close()

# file = open("myfiles.txt", "r")
# print(file.read())






# print("The total number of htm files are",htmCounter,"\n" "The files are", htmfile_Name)
# print("The total number of htm files are",htmlCounter,"\n" "The files are", htmlfile_Name)
# print("The total number of htm files are",pdfCounter,"\n" "The files are", pdffile_Name)
# print("The total number of htm files are",zipCounter,"\n" "The files are", zipfile_Name)



#print("Files and directories in '", path, "' :")
