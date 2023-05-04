from person import Person


class Student(Person):

    def __init__(self, first_name, last_name, address, phone, email, birthday, gpa):
        super().__init__(first_name, last_name, address, phone, email, birthday)
        self.gpa = gpa

    def __str__(self):
        student_info = super().__str__()  # Get the Person's __str__ output
        student_info += f"\nGPA: {self.gpa}"
        return student_info
