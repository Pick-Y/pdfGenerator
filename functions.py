from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path


# def generatePdfHeader(invNumber, invoiceDate):
    
    #  self.pdf = FPDF("P")
    #  self.pdf.add_page()

    #  self.pdf.set_font('Times', 'B', 16)
    #  self.pdf.cell(70,8,f"Invoice number:{invNumber}",ln=1)

    #  self.pdf.set_font('Times', 'B', 16)
    #  self.pdf.cell(50,8,f"Date: {invoiceDate}",ln=1)
   
    #  return self.pdf

class Pdf_invoice ():
    def __init__(self,invNumber,invDate,filePath):
        super().__init__()
        self.pdf = FPDF('P')
        self.invoice_number = invNumber
        self.date = invDate
        self.path = filePath
        self.df = pd.read_excel(self.path, sheet_name="Sheet 1")
    
    def generateHeader(self):
        self.pdf.add_page()
        self.pdf.set_font('Times', 'B', 16)
        self.pdf.cell(70,8,f"Invoice number:{self.invoice_number}",ln=1)

        self.pdf.set_font('Times', 'B', 16)
        self.pdf.cell(50,8,f"Date: {self.date}",ln=1)

        return self.pdf
    
    def setColumNames(self):
        df = pd.read_excel(self.path, sheet_name="Sheet 1")
    
        columns = list(df.columns)
        column_replaced = [item.title().replace("_"," ") for item in columns]

        self.pdf.set_font(family="Times", size=10,style="B")
        self.pdf.set_text_color(0,0,0)
        self.pdf.cell(20,8,column_replaced[0],border=1)
        self.pdf.cell(50,8,column_replaced[1], border=1)
        self.pdf.cell(30,8,column_replaced[2][0:6],border=1)
        self.pdf.cell(30,8,column_replaced[3],border=1)
        self.pdf.cell(30,8,column_replaced[4],border=1,ln=1)
    
    def fillTable(self):
        for index,row in self.df.iterrows():
       
            self.pdf.set_font(family="Times", size=10)
            self.pdf.set_text_color(80,80,80)
        
            self.pdf.cell(20,8,str(row['product_id']),border=1)
            self.pdf.cell(50,8,str(row['product_name']), border=1)
            self.pdf.cell(30,8,str(row['amount_purchased']),border=1)
            self.pdf.cell(30,8,str(row['price_per_unit']),border=1)
            self.pdf.cell(30,8,str(row['total_price']),border=1, ln=1)

    def printAmountDue(self):
        total = self.df['total_price'].sum()
        self.pdf.set_font(family="Times", size=10)
        self.pdf.set_text_color(0,0,0)
        self.pdf.cell(30,40,f"The total amount due is {total}") 

    def pdf_output(self):
        newString = self.invoice_number + "-" + self.date
        self.pdf.output(f'pdfs/{newString}.pdf', 'F')

