import openpyxl
import json
 

# Initialize a dictionary to store column widths and their frequencies
column_widths = {}
Excel = openpyxl.load_workbook("C:\\Users\\Mayilraj\\Downloads\\Test123\\User_Role_Product_Company_Mapiing_Grid.xlsx")
WS = Excel["Sheet2"]
 
# Iterate through columns and record their widths
for column_letter, column_dim in WS.column_dimensions.items():
    column_width = column_letter, column_dim.width
    if column_width in column_widths:
        column_widths[column_width] += 1
    else:
        column_widths[column_width] = 1
 
# Convert the dictionary to a list of dictionaries
column_data = [{"width": width} for width in column_widths.items()]
 
# Save the data to a JSON file
with open("C:\\Users\\Mayilraj\\Downloads\\Test123\\sample.json", "w") as outfile:
    json.dump(column_data, outfile, indent=4)