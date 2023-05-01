from file_read_admins import read_admin
from file_read_courses import read_courses
from file_read_students import read_students
from file_read_deps import read_deps
from undergraduate import Undergraduate
from graduate import Graduate
from admin import Admin
from department import Department
from course import Course

def sort_alphabetically(dict_to_sort):
    for k, v in dict_to_sort.items():
        if isinstance(v, Admin):
            sorted_dict = {k: v for k, v in sorted(dict_to_sort.items(), key=lambda item: item[1].first_name)}
        elif isinstance(v, Course):
            sorted_dict = {k: v for k, v in sorted(dict_to_sort.items(), key=lambda item: item[1].course_id)}
        elif isinstance(v, Department):
            sorted_dict = {k: v for k, v in sorted(dict_to_sort.items(), key=lambda item: item[1].name)}
        elif isinstance(v, Undergraduate):
            sorted_dict = {k: v for k, v in sorted(dict_to_sort.items(), key=lambda item: item[1].first_name)}
    for k, v in sorted_dict.items():
        print(k)






