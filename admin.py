from person import Person


class Admin(Person):
    def __init__(self, first_name, last_name, address, phone, email, birthday, department, courses_taught, salary):
        super().__init__(first_name, last_name, address, phone, email, birthday)
        self.department = department
        self.courses_taught = courses_taught
        self.salary = salary

