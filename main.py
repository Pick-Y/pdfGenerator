from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path


#Create a filepath for all files ending in xlsx

filepaths = glob.glob("invoices/*.xlsx")

#Create loop to loop through paths stored in filepaths
for filepath in filepaths:
    
   
    pdf = FPDF("P")
    pdf.add_page()
    #Extract the invoice number
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")  

    pdf.set_font('Times', 'B', 16)
    pdf.cell(70,8,f"Invoice number:{invoice_nr}",ln=1)

    pdf.set_font('Times', 'B', 16)
    pdf.cell(50,8,f"Date: {date}",ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    columns = list(df.columns)
    column_replaced = [item.title().replace("_"," ") for item in columns]

pdf.output(f'pdfs/invoice-{invoice_nr}.pdf', 'F')