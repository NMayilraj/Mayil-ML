import tkinter as tk
import tkinter.filedialog
from tkinter import*
import nbformat
import os
from nbconvert import PythonExporter

# Function to run Jupyter Notebook code
def run_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as notebook_file:
        notebook_content = notebook_file.read()

    notebook = nbformat.reads(notebook_content, as_version=4)
    python_exporter = PythonExporter()
    python_code, _ = python_exporter.from_notebook_node(notebook)

    exec(python_code, globals())

# Specify the path to your notebook
notebook_path = r'C:\Users\Mayilraj\Documents\Learning\Practices\IcecreamRevenue.ipynb'
print(os.path.exists(notebook_path))
# Run the Jupyter Notebook code
xi = run_notebook(notebook_path)

# Now you can use functions or variables defined in the notebook
result = xi
print(result)



class icecreamprice:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Ice cream Price")
        self.root.geometry("500x150")
        # Create a Text widget for the folder name textbox.
        Folderpath_name = Label(self.root, text = "Enter your required ice cream in grams:").place(x = 40, y = 30)
        self.folder_name_textbox = tk.Text(self.root, height=1, width=10)
        self.folder_name_textbox.place(x = 275, y = 33)

        # Create a Button widget to trigger the folder selection dialog.
  
        
        self.Submit_button = tk.Button(self.root, text="Check price", command=Pre_Rev)
        self.Submit_button.place(x = 390, y = 30)  
        

        

        # Start the mainloop.
        self.root.mainloop()
        tkinter.messagebox.showinfo("Welcome to GFG.",  Pre_Rev)

    
if __name__ == "__main__":
    folder_selection_window = icecreamprice()

