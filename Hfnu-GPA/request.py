import requests
import config
import const


class Request:
    def __init__(self):
        self.cookie = config.cookie
        self.user_agent = const.USER_AGENT
        self.data = const.DATA
        self.url = const.URL

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
        response = requests.get(self.url, headers=headers, params=self.data)
        """
        对response的状态进行异常处理
        """
        return response

    def get_text(self):
        return self.get_response().text
