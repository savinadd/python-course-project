class Course:
    def __init__(self, course_name, course_id, course_dep, course_prof, start_date, end_date, max_course_size):
        self.course_name = course_name
        self.course_id = course_id
        self.course_dep = course_dep
        self.course_prof = course_prof
        self.start_date = start_date
        self.end_date = end_date
        self.max_course_size = max_course_size
        self.list_of_students = []

    def __str__(self):
        course_info = f"{self.course_name} ({self.course_id})\n"
        course_info += f"Department: {self.course_dep}\n"
        course_info += f"Instructor: {self.course_prof}\n"
        course_info += f"Start Date: {self.start_date}\n"
        course_info += f"End Date: {self.end_date}\n"
        course_info += f"Max Course Size: {self.max_course_size}\n"
        course_info += f"Number of Students: {len(self.list_of_students)}\n"
        return course_info

    def add_student(self, student):
        self.list_of_students.append(student)

    def remove_student(self, student):
        self.list_of_students.remove(student)
