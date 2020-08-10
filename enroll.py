from course import Course
from student import Student
from datetime import datetime
def Error(str):
    print(str)

class Enroll:
    def __init__(self, student, course, grade, date):
        if not isinstance(student, Student):
            raise Error("invalid student...")
        if not isinstance(course, Course):
            raise Error("invalid course...")

        self.student = student
        self.course = course
        self.grade = grade
        self.date = datetime.now()

    def set_grade(self, grade):
        self.grade = grade
