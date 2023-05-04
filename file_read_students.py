from undergraduate import Undergraduate
from graduate import Graduate
from file_read_courses import read_courses
from file_read_admins import read_admin
import constant


def read_students():
    """
           Returns a dictionary of students, read from the input file.

                   Returns:
                           students (dict): Dictionary with the keys being the
                           student name and the value being the corresponding
                           Student object
    """
    admins = read_admin()
    students = {}
    courses = read_courses()
    departments = {}
    not_yet_read_dep = []
    not_yet_read_course = []
    not_yet_read_admin = []

    try:
        with open(constant.STUDENT_FILE, "r") as stu_file:
            for line in stu_file:
                data = line.strip().split("|")
                if data[0] == "STUDENT":
                    if data[1] == "Undergraduate":
                        first_name = data[2]
                        last_name = data[3]
                        address = data[4]
                        phone = data[5]
                        email = data[6]
                        birthday = data[7]
                        gpa = data[8]
                        major = data[9]
                        proj_grad_date = data[10]
                        year = data[11]
                        credits_completed = data[12]
                        current_courses = [course.strip() for course in data[13].split(',')]

                        undergrad = Undergraduate(first_name, last_name, address, phone, email,
                                                  birthday, gpa, major, proj_grad_date, year, credits_completed)
                        undergrad.set_current_courses(current_courses)
                        students[first_name + ' ' + last_name] = undergrad

                    elif data[1] == "Graduate":
                        first_name = data[2]
                        last_name = data[3]
                        address = data[4]
                        phone = data[5]
                        email = data[6]
                        birthday = data[7]
                        gpa = data[8]
                        thesis_topic = data[9]
                        thesis_advisor_name = data[10]
                        if thesis_advisor_name in admins:
                            thesis_advisor = admins[thesis_advisor_name]
                        else:
                            # handle case where admin has not been read yet
                            not_yet_read_admin.append(thesis_advisor_name)
                        grad = Graduate(first_name, last_name, address, phone, email,
                                        birthday, gpa, thesis_topic, thesis_advisor)

                        students[first_name + ' ' + last_name] = grad

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

        return students

    except FileNotFoundError:
        print("The input file with student info could not be found.")
