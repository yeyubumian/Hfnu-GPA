class Course:
    date_year: str
    date_semester = int
    name = str
    course_type = str
    credits = float
    GPA = float

    def __init__(self, date_year, date_semester, name, course_type, credits, GPA):
        self.date_year = date_year
        self.date_semester = date_semester
        self.name = name
        self.course_type = course_type
        self.credits = credits
        self.GPA = GPA