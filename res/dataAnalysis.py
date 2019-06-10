import xlrd

class TestData(object):
	CASE_PATH = '../res/vinData.xlsx'
#
	def __init__(self):
		source_excel = xlrd.open_workbook(self.CASE_PATH)
		self.data_sheet = source_excel.sheet_by_name('Sheet1')
		self.rows_count = self.data_sheet.nrows
		self.rows_index = 1
		self.case_data = []

	def analysis_data(self): #遍历excel，取出每一行的vin和partName作为数组中的元素，并逐一添加到空数组中
		temp_data = dict()
		for i in  range(1,self.rows_count):
			if temp_data != '':
				temp_data['vin'] = self.data_sheet.cell(i,0).value
				temp_data[ 'partName' ] = self.data_sheet.cell(i,5).value
				self.__case_data(temp_data)
	def __case_data(self,data):
		if data:
			self.case_data.append(data.copy())

	def get_case_data(self):
		return self.case_data



# if __name__ == '__main__':
# 	testDate = TestData()
# 	testDate.analysis_data()
# 	print(testDate.get_case_data())
