from person import Person
from course import Course

class Student(Person):

    def __init__(self, first_name, last_name, address, phone, email, birthday, gpa, major,
                 current_courses, proj_grad_date):
        super().__init__(first_name, last_name, address, phone, email, birthday)
        self.gpa = gpa
        self.major = major
        self.current_courses = []
        self.proj_grad_date = proj_grad_date

    def get_gpa(self):
        return self.gpa

    def get_major(self):
        return self.major

    def get_current_courses(self):
        return self.current_courses

    def get_proj_grad_date(self):
        return self.proj_grad_date

    def add_course(self, course_to_add):
        self.current_courses.append(course_to_add)
        course_to_add.add_student(self)