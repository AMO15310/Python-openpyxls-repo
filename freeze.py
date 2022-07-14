from openpyxl import Workbook
from openpyxl.styles import Alignment
wb =Workbook()
sheet = wb.active
sheet.freeze_panes='A1'
wb.save('freeze.xlsx')
