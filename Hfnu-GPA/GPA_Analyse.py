import HtmlParse
from Course import Course
import tools


class GPA_Analyse:
    def __init__(self):
        self.course_list = []

    def get_course_list(self):
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
        name_max = 0
        type_max = 0
        for course in self.course_list:
            name_max = max(name_max, len(course.name))
            type_max = max(type_max, len(course.course_type))
        with open('../data/我的成绩.txt', 'w', encoding="UTF-8") as file:
            for course in self.course_list:
                file.write(course.name)
                for i in range(name_max - len(course.name)):
                    file.write(' ')
                file.write(' ')
                file.write(course.course_type)
                file.write(' ')
                file.write("学分: " + str(course.credits) + " " + "绩点: " + str(course.GPA) + "\n")

