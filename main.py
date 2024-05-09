import requests
from bs4 import BeautifulSoup

class My_Grade:
    def __init__(self):
        self.soup = None
        self.response = None
        self.User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
        self.url = "https://jw.hfnu.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR"
        self.data = {"projectType": "MAJOR"}
        self.headers = None
        self.cookie = None
        self.My_Course = []
        self.get_cookie()
        self.get_headers()
        self.get_response()
        self.get_soup()
        self.write_grade()
        self.get_course()

    def get_cookie(self):
        self.cookie = input("请输入Cookie:")
        if not self.cookie:
            self.cookie = input()

    def get_headers(self):
        self.headers = {
            "Cookie": self.cookie,
            "User-Agent": self.User_Agent
        }

    def get_response(self):
        self.response = requests.get(self.url, params=self.data, headers=self.headers)

    def get_soup(self):
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def get_grade(self):
        all_td = (self.soup.find_all("tbody", id="grid19352773161_data"))
        return all_td

    def write_grade(self):
        grade = self.get_grade()
        with open("My_Grade.txt", "w", encoding="UTF-8") as f:
            for td in grade:
                f.write(td.get_text())

    def get_course(self):
        it = self.course()
        file = "My_Grade.txt"
        with open(file, "r", encoding="UTF-8") as f:
            x = 0
            for line in f:
                line = line.strip()
                if "-" in line:
                    x = 0
                    if it.name:
                        self.My_Course.append(it)
                if x == 0:
                    it = self.course()
                    it.date_year = line.split(' ')[0]
                    it.date_semester = int(line.split(' ')[1])
                    x += 1
                elif x == 1 or x == 2:
                    x += 1
                elif x == 3:
                    it.name = line
                    x += 1
                elif "课程" in line:
                    it.course_type = line.split(' ')[0]
                    it.credits = float(line.split(' ')[1])
                elif line != '\n' and line != '' and line != '通过' and line != '不通过' and line != '良好':
                    it.GPA = float(line)
        if it.name:
            self.My_Course.append(it)

    def get_average(self):
        ls = self.My_Course
        year = input("请输入学年(2022-2023):")
        semester = int(input("请输入学期(1/2):"))
        print("共有以下课程：")
        for i in ls:
            if i.date_year == year and i.date_semester == semester:
                print(i.name + " 类型：" + i.course_type + " 学分：" + str(i.credits) + " 绩点：" + str(i.GPA))

        print("")

        dict = {"1" : "专业基础课程", "2" : "专业核心课程", "3" : "通识选修课程", "4" : "通识必修课程", "5" : "校园文化与社会实践课程", "6" : "创新创业与学术科技课程", "7" : "综合实践课程"}
        print(dict)
        print("")
        ll = input("请输入要剔除计算的课程编号(空格分隔，0代表不剔除)：").split(' ')
        print("")
        ln = []
        for i in ll:
            if i in dict:
                ln.append(dict[i])

        x = 0
        sum = 0
        for i in ls:
            if i.date_year == year and i.date_semester == semester and i.course_type not in ln:
                x += i.credits
                sum += i.GPA * i.credits
        if sum == 0 or x == 0:
            return 0
        return sum / x


if __name__ == '__main__':
    my_grade = My_Grade()
    average = my_grade.get_average()
    print("平均绩点为：" + str(average))
