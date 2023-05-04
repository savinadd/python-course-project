from undergraduate import Undergraduate
from admin import Admin
from department import Department
from course import Course


def sort_alphabetically(dict_to_sort):
    """
       Returns an alphabetically sorted dictionary.

               Parameters:
                       dict_to_sort(dict): A dictionary of items chosen by the user

               Returns:
                       sorted_dict(dict): An alphabetically sorted dict.
    """
    sorted_dict = {}
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
        print(k + "\n")
    return sorted_dict
