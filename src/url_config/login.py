import json
import ssl
from urllib import request, parse

from src.url_config.url_parent import UrlRequest


class Login(UrlRequest):
    url = "https://api.dataenlighten.com:7045/oauth/loginByPhoneNum?"

    def _create_data(self, data=dict):
        login_data = dict()
        login_data['appType'] = 1
        login_data['code'] = '000000'
        login_data['phoneNum'] = '14100000000'
        login_data['productCode'] = 'I0101'
        login_data['version'] = '3.0.0'
        return login_data

    def _data_request(self, login_data):
        ssl._create_default_https_context = ssl._create_unverified_context
        login_data = parse.urlencode(login_data).encode('utf-8')
        req = request.Request(self.url, data=login_data)
        page = request.urlopen(req).read()
        page = page.decode('utf-8')
        return json.loads(page)

    def response(self, data=dict):
        UrlRequest.response(self,data)
        UrlRequest.header = self.__create_headers()

    def __get_token(self):
        return self.data['Content']['AccessToken']

    def __create_headers(self):
        token = self.__get_token()
        header_data = dict()
        token_value = "bearer %s" % token
        header_data['Authorization'] = token_value
        header_data['Content-Type'] = 'application/json;charset=utf-8'
        header_data['Accept - Language'] = 'zh - Hans - CN;q = 1, en - CN;q = 0.9, en - US;q = 0.8'
        header_data['Content - Length'] = 307
        header_data['User - Agent'] = 'MJDamageAssessmentApp / 2.3.0(iPhone;iOS11.3;Scale / 3.00)'
        header_data['Accept'] = '*/*'
        header_data['Connection'] = 'keep-alive'
        header_data['UserInfo'] = '13123456789, iOS, 11.300000, 2.3.0,, MJ_EMPLOYEE'
        header_data['Accept-Encoding'] = 'gzip,deflate'
        return header_data

# if __name__ == '__main__':
#     login = Login()
#     login.response()