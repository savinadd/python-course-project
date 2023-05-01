from undergraduate import Undergraduate
from graduate import Graduate
from admin import Admin
from department import Department
from course import Course


def read_courses():
    admins = {}
    undergrad_students = []
    grad_students = []
    courses = {}
    departments = {}
    not_yet_read_dep = []
    not_yet_read_course = []
    not_yet_read_admin = []

    COURSES_FILE = "courses.txt"

    try:
        with open(COURSES_FILE, "r") as course_file:
            for line in course_file:
                data = line.strip().split("|")
                if data[0] == "COURSE":
                    course_name = data[1]
                    course_id = data[2]
                    course_dep = data[3]
                    if course_dep not in departments:
                        not_yet_read_dep.append(course_dep)
                    else:
                        course_dep = departments[course_dep]
                    course_prof = data[4]
                    if course_prof not in admins:
                        not_yet_read_admin.append(course_prof)
                    else:
                        course_prof = admins[course_prof]
                    start_date = data[5]
                    end_date = data[6]
                    max_course_size = data[7]

                    course = Course(course_name, course_id, course_dep, course_prof, start_date, end_date,
                                    max_course_size)
                    courses[course_id] = course

            # Remove duplicate keys from the courses dictionary
            courses = dict(set(courses.items()))


            return courses

    except FileNotFoundError:
        print("The file 'admins.txt' could not be found.")
