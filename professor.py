from person import Person
from course import Course

class Professor(Person):
    def __init__(self, first, last, dob, phone, address, salary):
        super.__init__(self, first, last, dob, phone, address)
        self.salary = salary
        self.courses = []
        self.got_raise = False

    def check_for_raise(self):
        if len(self.courses) >= 4:
            self.salary += 20000
            self.got_raise = True

    def add_course(self, course):
        if not isinstance(course, Course):
            raise Error("Invalid course...")

        self.courses.append(course)
