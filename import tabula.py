import tabula
import camelot

# Specify the path to your PDF file
pdf_path = "C:\\Users\\Mayilraj\\Downloads\\form-d-xml-tech-specs-12 (1)\\EDGAR Form D XML Technical Specification.pdf"

# Specify the output Excel file path
excel_output_path = "C:\\Users\\Mayilraj\\Downloads\\form-d-xml-tech-specs-12 (1)\\output_excel_file.xlsx"

# Use camelot-py as the backend for tabula-py
tabula.io.guess = lambda f, **kwargs: "camelot"

# Use tabula to extract tables from the PDF
tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

# If there are multiple tables, you may want to loop through them
for i, table in enumerate(tables):
    # Save each table to a separate sheet in the Excel file
    sheet_name = f"Table_{i+1}"
    table.to_excel(excel_output_path, sheet_name=sheet_name, index=False)
