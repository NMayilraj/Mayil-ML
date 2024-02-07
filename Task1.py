import os
import glob
from tkinter import messagebox
path = "C:\\Users\\Mayilraj\\Documents\\Learning\\Search"
dir_list = os.listdir(path)


def create_list(Exp):
    file_Name = glob.glob1(path,Exp)
    fileCounter = len(file_Name)
    Result = "The total number of "+ Exp.replace("*.","") +" files are " + str(fileCounter) + "\nThe files are below\n"
    Res = ""
    coumter = 1
    for hf in file_Name:
        Res = Res + str(coumter) + ". "+ path + "\\" + hf + '\n'
        coumter += 1
    R1 = Result + str(Res)
    return R1

Content = create_list("*.html") + "\n" + create_list("*.pdf") + "\n" + create_list("*.zip") + "\n" + create_list("*.htm") + "\n" +create_list("*.txt")


def wr():
    file = open("myfiles.txt","w")
    file.write(Content)
    file.close()  
    messagebox.showinfo('Info', 'Process completed!')


