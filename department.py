from colorama import Fore, Style


class Department:
    def __init__(self, name, chair, courses_of_dep):
        self.name = name
        self.chair = chair
        self.courses_of_dep = courses_of_dep

    def __str__(self):
        department_info = f"\n{Fore.YELLOW}{self.name} Department\n"
        department_info += f"{Style.RESET_ALL}Chair: {Fore.LIGHTBLUE_EX}{self.chair}\n"
        department_info += f"{Style.RESET_ALL}Courses Offered: {', '.join(self.courses_of_dep)}\n"
        return department_info
