from person import Person
from course import Course


class Student(Person):

    def __init__(self, first_name, last_name, address, phone, email, birthday, gpa):
        super().__init__(first_name, last_name, address, phone, email, birthday)
        self.gpa = gpa
        self.courses = []

    def __str__(self):
        student_info = super().__str__()  # Get the Person's __str__ output
        student_info += f"\nGPA: {self.gpa:.2f}"
        student_info += f"\nCourses: {', '.join(self.courses)}" if self.courses else ""  # Add courses if available
        return student_info


    def get_gpa(self):
        return self.gpa

    def get_major(self):
        return self.major

    def add_course(self, course_to_add):
        if course_to_add not in self.courses:
            self.courses.append(course_to_add)
        course_to_add.add_student(self)

    def remove_course(self, course_to_remove):
        if course_to_remove in self.courses:
            self.courses.remove(course_to_remove)
        course_to_remove.remove_student(self)