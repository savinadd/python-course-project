from student import Student


class Undergraduate(Student):

    CREDITS_TO_GRAD = 120

    def __init__(self, first_name, last_name, address, phone, email, birthday, gpa, major,
                 proj_grad_date, year, credits_completed, current_courses):
        super().__init__(first_name, last_name, address, phone, email, birthday, gpa)
        self.major = major
        self.proj_grad_date = proj_grad_date
        self.year = year
        self.credits_completed = credits_completed
        self.current_courses = []

    def __str__(self):
        return super().__str__() + f"\nMajor: {self.major}\nProjected Graduation Date: {self.proj_grad_date}\nYear: {self.year}\nCredits Completed: {self.credits_completed}\nCurrent Courses: {self.current_courses}"





