from person import Person


class Student(Person):
    """
        A class to represent a student.

        ...

        Attributes
        ----------
        f_name : str
        first name of the student
        l_name : str
        last name of the student
        address : str
        address of student
        phone : str
        phone number
        email : str
        email of student
        birthday : str
        birthday of student
        gpa : str
        gpa of the student
        """
    def __init__(self, first_name, last_name, address, phone, email, birthday, gpa):
        super().__init__(first_name, last_name, address, phone, email, birthday)
        self.gpa = gpa

    def __str__(self):
        student_info = super().__str__()
        student_info += f"\nGPA: {self.gpa}"
        return student_info
