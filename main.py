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

pdf.output(f'pdfs/invoice-{invoice_nr}.pdf', 'F')