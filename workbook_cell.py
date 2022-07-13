import time
from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
now = time.strftime('%x')


sheet['A1']="Date"
sheet.cell(row=2,column=1).value=now
wb.save(r'/home/samo/github_files/workbook_cell.xlsx')


