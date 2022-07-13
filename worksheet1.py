import time 
from openpyxl import Workbook
# import the workbook module and define it as wb
wb = Workbook()
#define sheet
sheet  = wb.active
#define now as the date today
now = time.strftime("%x")
#input the sheet values
sheet['A1']=now
sheet['A2']=98
sheet['A3']=108
sheet['A4']=96
sheet['A5']=56
sheet['A6']=89
#save the sheet
wb.save('sales_today')

