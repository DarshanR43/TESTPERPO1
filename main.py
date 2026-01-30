# registration_half.py
# Weak structure, partial logic, tightly coupled, missing validations

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course_name):
        self.courses.append(course_name)


class Course:
    def __init__(self, title):
        self.title = title


class RegistrationSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, name):
        s = Student(name)
        self.students.append(s)

    def add_course(self, title):
        c = Course(title)
        self.courses.append(c)

    def register(self, student_name, course_title):
        # messy search logic
        for s in self.students:
            if s.name == student_name:
                s.add_course(course_title)


# ---- usage ----
if __name__ == "__main__":
    system = RegistrationSystem()
    system.add_student("Alice")
    system.add_course("Math")

    system.register("Alice", "Math")
