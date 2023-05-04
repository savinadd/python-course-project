from student import Student


class Undergraduate(Student):
    """
           A class to represent an Undergraduate student.

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
           major : str
           major of the student
           proj grad date: str
           projected graduation date of the student
           year : str
           year of school, in a numbered version, not word
           credits_completed : str
           number of credits completed
           current_courses : list
           list of courses
           """
    def __init__(self, first_name, last_name, address, phone, email, birthday, gpa, major,
                 proj_grad_date, year, credits_completed, current_courses=None):
        super().__init__(first_name, last_name, address, phone, email, birthday, gpa)
        self.major = major
        self.proj_grad_date = proj_grad_date
        self.year = year
        self.credits_completed = credits_completed
        self.current_courses = []

    def set_current_courses(self, current_courses):
        self.current_courses = current_courses

    def __str__(self):
        current_courses_str = ', '.join(self.current_courses)
        return f"{super().__str__()}\nMajor: {self.major}\nProjected Graduation Date: {self.proj_grad_date}\n" \
               f"Year: {self.year}\nCredits Completed: {self.credits_completed}\n" \
               f"Current Courses: {current_courses_str}\n"
