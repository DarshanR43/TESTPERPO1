# registration_full.py
# Clean OOP, proper relationships, validation, modular design

from typing import List


class Course:
    def __init__(self, course_id: str, title: str, capacity: int):
        self.course_id = course_id
        self.title = title
        self.capacity = capacity
        self.students: List["Student"] = []

    def has_seat(self) -> bool:
        return len(self.students) < self.capacity

    def enroll(self, student: "Student"):
        if not self.has_seat():
            raise Exception("Course full")

        self.students.append(student)


class Student:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.courses: List[Course] = []

    def register_course(self, course: Course):
        course.enroll(self)
        self.courses.append(course)


class RegistrationManager:
    def __init__(self):
        self.students: dict[str, Student] = {}
        self.courses: dict[str, Course] = {}

    def add_student(self, student_id: str, name: str):
        self.students[student_id] = Student(student_id, name)

    def add_course(self, course_id: str, title: str, capacity: int):
        self.courses[course_id] = Course(course_id, title, capacity)

    def register(self, student_id: str, course_id: str):
        student = self.students[student_id]
        course = self.courses[course_id]
        student.register_course(course)

    def list_student_courses(self, student_id: str):
        student = self.students[student_id]
        return [c.title for c in student.courses]


# ---- usage ----
if __name__ == "__main__":
    manager = RegistrationManager()

    manager.add_student("S1", "Alice")
    manager.add_course("C1", "Math", 2)
    manager.register("S1", "C1")


    print(manager.list_student_courses("S1"))
