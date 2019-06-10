from src.url_config.url_parent import UrlRequest


class VinQuery(UrlRequest):
	url = 'https://api.dataenlighten.com:7045/aida/vehicle/vinQuery'

	def _create_data(self,data ):
		vin_data = {
			"version": "1.2.0",
			"vinCode": data,
			"partRange": 2,
			"onlineBrandTimeOut": 10
		}
		return vin_data
