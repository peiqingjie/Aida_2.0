from src.url_config.login import Login
from src.url_config.vinQuery import VinQuery
from res.dataAnalysis import TestData

if __name__ == '__main__':
	test_data = TestData()
	test_data.analysis_data()
	case_data = test_data.get_case_data()
	login = Login()
	login.response()
	vinQuery = VinQuery()

	for case in case_data:
		vin = case['vin']
		partName = case['partName']
		vinQuery.response(vin)

