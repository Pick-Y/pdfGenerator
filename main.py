from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path
from functions import *


#Create a filepath for all files ending in xlsx
filepaths = glob.glob("invoices/*.xlsx")




for filepath in filepaths:
   
     filename = Path(filepath).stem
    
     invoice_nr, date = filename.split("-")  
     
     pdf = Pdf_invoice(invoice_nr,date,filepath)
     
     pdf.generateHeader()

     pdf.setColumNames()

     pdf.fillTable()

     pdf.printAmountDue()


     pdf.pdf_output()
