from undergraduate import Undergraduate
from graduate import Graduate
from admin import Admin
from department import Department
from course import Course


def read_admin():
    admins = {}
    undergrad_students = []
    grad_students = []
    courses = {}
    departments = {}
    not_yet_read_dep = []
    not_yet_read_course = []
    not_yet_read_admin = []

    ADMIN_FILE = "admins.txt"

    try:
        with open(ADMIN_FILE, "r") as admin_file:
            for line in admin_file:
                data = line.strip().split("|")
                if data[0] == "ADMIN":
                    first_name = data[1]
                    last_name = data[2]
                    address = data[3]
                    phone = data[4]
                    email = data[5]
                    birthday = data[6]
                    department_name = data[7]
                    courses_taught = data[8].split(',')
                    salary = 500

                    admin = Admin(first_name, last_name, address, phone, email,
                                  birthday, department_name, courses_taught, salary)
                    key = first_name + " " + last_name

                    if key not in admins:
                        admins[key] = admin

                    while not_yet_read_admin:
                        admin_name = not_yet_read_admin.pop()
                        if admin_name in admins:
                            admin = admins[admin_name]
                            dept_name = admin.get_department()
                            if dept_name in departments:
                                dept = departments[dept_name]
                            else:
                                not_yet_read_dep.append(dept_name)
                            courses_taught = admin.get_courses_taught()
                            course_list = []
                            for course_id in courses_taught:
                                if course_id in courses:
                                    course_list.append(courses[course_id])
                                else:
                                    not_yet_read_course.append(course_id)
                            admin.set_department(dept)
                            admin.set_courses_taught(course_list)
                            admins[admin_name] = admin

            admins = dict(set(admins.items()))

        return admins

    except FileNotFoundError:
        print("The file 'admins.txt' could not be found.")
