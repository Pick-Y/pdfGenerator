from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path


def generatePdfHeader(invNumber, invoiceDate):
    
    pdf = FPDF("P")
    pdf.add_page()

    pdf.set_font('Times', 'B', 16)
    pdf.cell(70,8,f"Invoice number:{invNumber}",ln=1)

    pdf.set_font('Times', 'B', 16)
    pdf.cell(50,8,f"Date: {invoiceDate}",ln=1)
   
    return pdf