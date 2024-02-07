import openpyxl
import json
 
# Initialize an empty list to store column widths
final = []
 
# Specify the path to your Excel file
excel_file_path = "C:\\Users\\Mayilraj\\Downloads\\Test123\\User_Role_Product_Company_Mapiing_Grid.xlsx"
 
# Load the Excel file

Excel = openpyxl.load_workbook(excel_file_path)
WS = Excel["Sheet2"]
# Iterate through columns and record their widths
for column_letter, column_dim in WS.column_dimensions.items():
    Excel = openpyxl.load_workbook(excel_file_path)
    
    column_width = column_letter, column_dim.width
    final.append(column_width)
 
# Save the data to a JSON file
json_object = json.dumps(final, indent=4)
with open("C:\\Users\\Mayilraj\\Downloads\\Test123\\sample.json", "w") as outfile:
    outfile.write(json_object)