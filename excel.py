# working with .xlsx files in python

import openpyxl
from pathlib import Path

file_path = Path("./files/example3.xlsx")
print(file_path)
wb = openpyxl.load_workbook("./files/example3.xlsx")
print(type(wb))