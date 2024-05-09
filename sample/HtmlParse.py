import Request
from bs4 import BeautifulSoup


class HtmlParse:
    def __init__(self):
        self.text = Request.Request().get_text()

    def get_soup(self):
        return BeautifulSoup(self.text, 'html.parser')

    def get_grade_list(self):
        soup = self.get_soup()
        return soup.find_all("tbody", id="grid19352773161_data")

    def write_grade_list(self):
        grade_list = self.get_grade_list()
        with open('../data/我的成绩.txt', 'w',encoding="UTF-8") as file:
            for grade in grade_list:
                file.write(grade.get_text())


