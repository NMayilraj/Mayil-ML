import openpyxl
import json
Excel = openpyxl.load_workbook("C:\\Users\\Mayilraj\\Downloads\\Test123\\User_Role_Product_Company_Mapiing_Grid.xlsx")
WS = Excel["Sheet2"]
Final = []
for column_letter, column_dim in WS.column_dimensions.items():
    column_width = column_letter, column_dim.width
    if column_width not in Final:
        Final.append(column_width)
json_object = json.dumps(Final, indent=4)

with open("C:\\Users\\Mayilraj\\Downloads\\Test123\\sample.json", "w") as outfile:
    outfile.write(json_object)

