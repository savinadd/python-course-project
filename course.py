from colorama import Fore, Style


class Course:
    def __init__(self, course_name, course_id, course_dep, course_prof, start_date, end_date, max_course_size):
        self.course_name = course_name
        self.course_id = course_id
        self.course_dep = course_dep
        self.course_prof = course_prof
        self.start_date = start_date
        self.end_date = end_date
        self.max_course_size = max_course_size

    def __str__(self):
        return f"\n{Fore.YELLOW}{self.course_name} {Style.RESET_ALL}({self.course_id})\n" \
               f"Department: {self.course_dep}\n" \
               f"Instructor: {self.course_prof}\n" \
               f"Start Date: {self.start_date}\n" \
               f"End Date: {self.end_date}\n" \
               f"Max Course Size: {self.max_course_size}\n"
