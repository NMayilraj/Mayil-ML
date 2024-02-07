import tkinter as tk
from tkinter import*
from Task1 import*
class FolderSelectionWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Folder Selection")
        self.root.geometry("600x150")
        # Create a Text widget for the folder name textbox.
        Folderpath_name = Label(self.root, text = "Folder Path").place(x = 40, y = 60)
        self.folder_name_textbox = tk.Text(self.root, height=1, width=20)
        self.folder_name_textbox.place(x = 110, y = 60)

        # Create a Button widget to trigger the folder selection dialog.
        self.select_folder_button = tk.Button(self.root, text="Browse", command=self.select_folder)
        self.select_folder_button.place(x = 310, y = 60)
        
        self.Submit_button = tk.Button(self.root, text="Submit", command=wr())
        self.Submit_button.place(x = 390, y = 60)
        
        # Start the mainloop.
        self.root.mainloop()

    def select_folder(self):
        # Open the folder selection dialog.
        folder_name = tk.filedialog.askdirectory(title="Select Folder")

        # Insert the selected folder name into the textbox.
        self.folder_name_textbox.insert("1.0", folder_name)

if __name__ == "__main__":
    folder_selection_window = FolderSelectionWindow()


