from person import Person


class Admin(Person):
    def __init__(self, first_name, last_name, address, phone, email, birthday, department, courses_taught, salary):
        super().__init__(first_name, last_name, address, phone, email, birthday)
        self.department = department
        self.courses_taught = courses_taught
        self.salary = salary

    def __str__(self):
        courses = [str(course) for course in self.courses_taught]
        return super().__str__() + f", Department: {self.department}, " \
                                   f"Courses Taught: {', '.join(courses)}, " \
                                   f"Salary: {self.salary}\n------------------------" \
                                   f"-------------------------------------------"
