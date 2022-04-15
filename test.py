import openpyxl

wb = openpyxl.load_workbook('people_low.xlsx')
# print(wb.sheetnames)
# print(wb.active)
sheet = wb['Sheet1']

for row in sheet.rows:
    print([cell.value for cell in row])