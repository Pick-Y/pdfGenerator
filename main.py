from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path


#Create a filepath for all files ending in xlsx

filepaths = glob.glob("invoices/*.xlsx")