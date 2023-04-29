from student import Student


class Graduate(Student):
    def __init__(self, first_name, last_name, address, phone, email, birthday, gpa, major,
                 current_courses, thesis_topic, thesis_advisor):
        super().__init__(self, first_name, last_name, address, phone, email, birthday, gpa, major,
                         current_courses)
        self.thesis_topic = thesis_topic
        self.thesis_advisor = thesis_advisor

