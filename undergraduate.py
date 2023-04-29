from student import Student


class Undergraduate(Student):

    CREDITS_TO_GRAD = 120

    def __init__(self, first_name, last_name, address, phone, email, birthday, gpa, major,
                 current_courses, proj_grad_date, year, credits_completed):
        super().__init__(first_name, last_name, address, phone, email, birthday, gpa, major,
                         current_courses, proj_grad_date)
        self.year = year
        self.credits_completed = credits_completed



