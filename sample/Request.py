import requests
import Constant


class Request:
    def __init__(self):
        self.cookie = Constant.cookie
        self.user_agent = Constant.User_Agent
        self.data = Constant.DATA

    def create_headers(self):
        """
        Cookie 不可用的异常处理
        """
        headers = {
            'Cookie': self.cookie,
            'User-Agent': self.user_agent
        }
        return headers

    def get_response(self):
        headers = self.create_headers()
        url = Constant.URL
        data = Constant.DATA
        response = requests.get(url, headers=headers, params=data)
        """
        对response的状态进行异常处理
        """
        return response.text
