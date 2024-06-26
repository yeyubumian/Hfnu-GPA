from course import Course
from html_parse import HtmlParse
import config
import tools


class GPA_Analyse:
    def __init__(self):
        self.course_list = []

    def get_course_list(self):
        HtmlParse().write_grade_list()
        it = Course()
        with open('../data/data.txt', 'r', encoding="UTF-8") as file:
            count = 0
            for line in file:
                line = line.strip()
                if "-" in line:
                    if count != 0:
                        self.course_list.append(it)
                        it = Course()
                    count = 0

                if count == 0:
                    it.date_year, it.date_semester = list(line.split(' '))
                    count += 1
                elif count < 3:
                    count += 1
                elif count == 3:
                    it.name = line
                    count += 1
                elif "课程" in line:
                    it.course_type = line.split(' ')[0]
                    it.credits = float(line.split(' ')[1])
                elif tools.is_number(line):
                    it.GPA = float(line)

            if count != 0:
                self.course_list.append(it)

    def write_course_list(self):
        self.get_course_list()
        with open('../data/我的成绩.txt', 'w', encoding="UTF-8") as file:
            for course in self.course_list:
                file.write(
                    course.name + " " + course.course_type + " 学年：" + course.date_year + " 学期：" + course.date_semester + " 学分：" + str(
                        course.credits) + " 绩点：" + str(course.GPA) + "\n")

    def analyse(self):
        self.write_course_list()
        date_year = config.date_year
        date_semester = ["1", "2"]
        if config.date_semester == "1":
            date_semester = "1"
        elif config.date_semester == "2":
            date_semester = "2"

        with open('../data/目标成绩分析', 'w', encoding="UTF-8") as file:
            credits_sum = 0
            GPA_sum = 0
            course_t = {"专业基础课程":1,"专业核心课程":2,"通识必修课程":3,"通识选修课程":4,"综合实践课程":5,"校园文化与社会实践课程":6,"创新创业与学术科技课程":7}
            course_c = []
            for i in course_t:
                if course_t[i] in config.course_list:
                    course_c.append(i)

            for course in self.course_list:
                if course.date_year == date_year and course.date_semester in date_semester and course.course_type in course_c:
                    credits_sum += course.credits
                    GPA_sum += course.GPA * course.credits
                    file.write(
                        course.name + " " + course.course_type + " 学分：" + str(
                            course.credits) + " 绩点：" + str(course.GPA) + "\n")
            average = GPA_sum / credits_sum
            file.write("平均绩点" + str(average) + "\n")
