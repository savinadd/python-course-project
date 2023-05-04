from person import Person


class Admin(Person):
    """
    A class to represent an administrator.

    ...

    Attributes
    ----------
    f_name : str
    first name of the admin
    l_name : str
    last name of the admin
    address : str
    address of admin
    phone : str
    phone number
    email : str
    email of admin
    birthday : str
    birthday of admin
    department : Department
    department that the admin is a part of
    courses_taught : dict
    key is the name of the course, value is the course object
    salary : str
    salary of the admin

    """

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
