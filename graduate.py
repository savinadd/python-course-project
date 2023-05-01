from student import Student

class Graduate(Student):
    def __init__(self, first_name, last_name, address, phone, email, birthday, gpa,
                 thesis_topic, thesis_advisor):
        super().__init__(first_name, last_name, address, phone, email, birthday,gpa)
        self.thesis_topic = thesis_topic
        self.thesis_advisor = thesis_advisor

    def __str__(self):
        return super().__str__() + f"\nGraduate Student: {self.first_name} {self.last_name} ;\tThesis Topic: {self.thesis_topic};\tThesis Advisor: {self.thesis_advisor.first_name} {self.thesis_advisor.last_name}"
