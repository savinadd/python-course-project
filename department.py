class Department:
    def __init__(self, name, chair, courses_of_dep):
        self.name = name
        self.chair = chair
        self.courses_of_dep = courses_of_dep

    def __str__(self):
        department_info = f"{self.name} Department\n"
        department_info += f"Chair: {self.chair}\n"
        department_info += f"Courses Offered: {', '.join(self.courses_of_dep)}\n"
        return department_info

