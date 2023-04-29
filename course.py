class Course:
    def __init__(self, course_name, course_id, course_dep, course_prof, start_date, end_date, max_course_size, list_of_students):
        self.course_name = course_name
        self.course_id = course_id
        self.course_dep = course_dep
        self.course_prof = course_prof
        self.start_date = start_date
        self.end_date = end_date
        self.max_course_size = max_course_size
        self.list_of_students = []

    def add_student(self, student):
        self.list_of_students.append(student)

    def remove_student(self, student):
        self.list_of_students.remove(student)
