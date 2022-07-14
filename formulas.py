from openpyxl import Workbook

wb = Workbook()
sheet = wb.active


rows=(
(14,58),
(56,58),
(89,580),
(78,12),
(56,54),
(45,89)


        )
for x in rows:
    sheet.append(x)


cell = sheet.cell(row=7,column=3)
cell.value = '=SUM(A1:B6)'
#cell.font = cell.font.copy(bold=True)
wb.save("formulas.xlsx")
