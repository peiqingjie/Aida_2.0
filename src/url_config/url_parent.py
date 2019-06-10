from  urllib import request
import json,ssl

class UrlRequest():
	header = {}
	url = ''
	data = {}

	def __init__(self):
		pass

	def _create_data(self,data):
		return data

#将header、url、 data整合且转为为json格式
	def _data_request(self,data):
		ssl._create_default_https_context = ssl._create_unverified_context
		key_data = json.dumps(data).encode('utf-8')
		req = request.Request(self.url, data=key_data, headers=UrlRequest.header)
		key = request.urlopen(req).read()
		key = key.decode('utf-8')
		return json.loads(key)

#执行接口请求
	def response(self,data=()):
		key_data = self._create_data(data)
		self.data = self._data_request(key_data)
		print(self.data)

