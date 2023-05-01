from undergraduate import Undergraduate
from graduate import Graduate
from admin import Admin
from department import Department
from course import Course


def read_deps():
    admins = {}
    undergrad_students = []
    grad_students = []
    courses = {}
    departments = {}
    not_yet_read_dep = []
    not_yet_read_course = []
    not_yet_read_admin = []


    DEPARTMENT_FILE = "departments.txt"


    try:
        with open(DEPARTMENT_FILE, "r") as dep_file:
            for line in dep_file:
                data = line.strip().split("|")
                if data[0] == "DEPARTMENT":
                    name = data[1]
                    chair = data[2]
                    if chair in admins:
                        chair = admins[data[1]]
                    else:
                        not_yet_read_admin.append(chair)
                    courses_of_dep = data[3].split(',')
                    course_list = []
                    for course_id in courses_of_dep:
                        if course_id in courses:
                            course_list.append(courses[course_id])
                        else:
                            not_yet_read_course.append(course_id)
                    if name not in departments:
                        dept = Department(name, chair, courses_of_dep)
                        departments[name] = dept
            while not_yet_read_dep:
                dep_name = not_yet_read_dep.pop()
                if dep_name in departments:
                    dept = departments[dep_name]
                    courses_of_dep = dept.get_courses()
                    course_list = []
                    for course_id in courses_of_dep:
                        if course_id in courses:
                            course_list.append(courses[course_id])
                        else:
                            not_yet_read_course.append(course_id)
                    dept.set_courses(course_list)
                    departments[dep_name] = dept
        return departments
    except FileNotFoundError:
        print("The file 'admins.txt' could not be found.")