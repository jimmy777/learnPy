import xlrd

data = xlrd.open_workbook('123.xls')

table = data.sheets()[0]

cell_A1 = table.cell(0,0).value

print cell_A1
