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

   

     

#     df = pd.read_excel(filepath, sheet_name="Sheet 1")
    
#     columns = list(df.columns)
#     column_replaced = [item.title().replace("_"," ") for item in columns]

#     pdf.set_font(family="Times", size=10,style="B")
#     pdf.set_text_color(0,0,0)
#     pdf.cell(20,8,column_replaced[0],border=1)
#     pdf.cell(50,8,column_replaced[1], border=1)
#     pdf.cell(30,8,column_replaced[2][0:6],border=1)
#     pdf.cell(30,8,column_replaced[3],border=1)
#     pdf.cell(30,8,column_replaced[4],border=1,ln=1)

#     for index,row in df.iterrows():
       
#         pdf.set_font(family="Times", size=10)
#         pdf.set_text_color(80,80,80)
       
#         pdf.cell(20,8,str(row['product_id']),border=1)
#         pdf.cell(50,8,str(row['product_name']), border=1)
#         pdf.cell(30,8,str(row['amount_purchased']),border=1)
#         pdf.cell(30,8,str(row['price_per_unit']),border=1)
#         pdf.cell(30,8,str(row['total_price']),border=1, ln=1)

#     total = df['total_price'].sum()
#     pdf.set_font(family="Times", size=10)
#     pdf.set_text_color(0,0,0)
#     pdf.cell(30,40,f"The total amount due is {total}") 

     pdf.pdf_output()
