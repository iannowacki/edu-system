from professor import Professor
from enroll import Enroll
class Course:
    def __init__(self, name, code, max_, min_, professor):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.professor = []
        self.enrollments = []

        if isinstance(professor, Professor):
            self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise Error("Invalid Professor...")
            self.professors = professor
        else:
            raise Error("Invalid Professor...")

    def add_professor(selfself, professor):
        if not isinstance(professor, Professor):
            raise Error("Invalid Professor...")

    def add_enrollments(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Error("Invalid Enrollment")
        if len(enrollments == self.max):
            raise Error("Cannot enroll, course full... ")

        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) < self.min