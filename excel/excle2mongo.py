import xlrd
import types
import pymongo
import sys  
reload(sys)  
sys.setdefaultencoding('utf8') 


cell_n = []
filename = ''

data = xlrd.open_workbook('No9floor.xls')
con = pymongo.Connection('127.0.0.1',27017)
db = con.floor

table = data.sheets()[0]
rows_n = table.nrows
cols_n = table.ncols

#creat a list contains how many cols
def creatList():
	i = 0
	while i < cols_n:
		cell_n.append([])
		i += 1

#put data to the list
def setData():
	i = 0
	while i < cols_n:
		j = 0
		while j < rows_n:
			current_cell = table.cell(j,i).value;
			if type(current_cell) is types.UnicodeType:
				cell_n[i].append(current_cell)
			if type(current_cell) is types.StringType:
				cell_n[i].append(current_cell)
			if type(current_cell) is types.FloatType:
				cell_n[i].append(int(current_cell))
			j += 1
		print '#####################################################'	
		i += 1

def setMongo():
	test = db.floorData
	test.drop()
	i = 0
	while i<rows_n:
		test.save({'id':i,'no':cell_n[1][i],'function':cell_n[2][i],'teach':cell_n[3][i]})
		i+=1

def main():
	creatList()
	setData()
	setMongo()

if __name__ == '__main__':
	main()