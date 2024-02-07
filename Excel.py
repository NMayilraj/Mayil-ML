import openpyxl

def same_text(text):
    Excel = openpyxl.load_workbook("C:\\Users\\Mayilraj\\Downloads\\Test123\\User_Role_Product_Company_Mapiing_Grid.xlsx")
    Ws = Excel.active
    Count =  {}
    for row in Ws.rows:
        for cell in row:
            if isinstance(cell.value, str):
                if cell.value in Count:
                    Count[cell.value] += 1
                else:
                    Count[cell.value] = 1
    text_count = Count.get(text, 0)
    return Count
print(same_text("N/A"))


