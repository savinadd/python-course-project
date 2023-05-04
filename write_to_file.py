from undergraduate import Undergraduate
from graduate import Graduate
from admin import Admin
from file_read_courses import read_courses
from file_read_admins import read_admin
from file_read_deps import read_deps
import constant
from colorama import Fore


def write_to_file(object_type):
    """
           Writes the desired information to an existing file.

                   Parameters:
                           object_type(str): A string inputted by the user of the type of object
                                             to be written
    """

    object_type = object_type.capitalize()
    if object_type == "Undergraduate":
        f_name = input("First name: ")
        l_name = input("Last name: ")
        address = input("Address: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        bday = input("Birthday: ")
        gpa = input("GPA: ")
        major = input("Major: ")
        proj_grad_date = input("Projected graduation date: ")
        year = input("Year: ")
        credits_completed = input("Credits completed (number): ")
        current_courses = []
        amt = int(input("How many classes will you be inputting? : "))
        for x in range(amt):
            course_id = input("If you enter in an incorrect class ID, it will NOT be added. Enter the class ID: ")
            for course in read_courses().values():
                if course.course_id == course_id:
                    current_courses.append(course)
        new_student = Undergraduate(f_name, l_name, address, phone, email, bday, gpa, major, proj_grad_date, year,
                                    credits_completed, current_courses)
        current_courses_str = ",".join([course.course_id for course in current_courses])
        try:
            with open(constant.STUDENT_FILE, "a") as f:
                f.write(
                    f"\nSTUDENT|Undergraduate|{new_student.first_name}|{new_student.last_name}|{new_student.address}|"
                    f"{new_student.phone}|{new_student.email}|{new_student.birthday}|{new_student.gpa}|"
                    f"{new_student.major}|"
                    f"{new_student.proj_grad_date}|{new_student.year}|{new_student.credits_completed}|"
                    f"{current_courses_str}")
        except FileNotFoundError:
            print("The input file with student info could not be found.")

    elif object_type == "Graduate":
        f_name = input("First name: ")
        l_name = input("Last name: ")
        address = input("Address: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        bday = input("Birthday: ")
        gpa = input("GPA: ")
        thesis_topic = input("Thesis topic: ")
        thesis_advisor_name = input("Thesis advisor name (first last): ")
        thesis_advisor = None
        for admin in read_admin().values():
            if admin.first_name + " " + admin.last_name == thesis_advisor_name:
                thesis_advisor = admin.first_name + " " + admin.last_name
                break
        if not thesis_advisor:
            print(Fore.RED + "This advisor does not exist. System will exit.")
            exit(1)
        new_student = Graduate(f_name, l_name, address, phone, email, bday, gpa, thesis_topic, thesis_advisor)
        try:
            with open(constant.STUDENT_FILE, "a") as f:
                f.write(
                    f"\nSTUDENT|Graduate|{new_student.first_name}|{new_student.last_name}|{new_student.address}"
                    f"|{new_student.phone}|{new_student.email}|{new_student.birthday}|{new_student.gpa}|"
                    f"{new_student.thesis_topic}|{new_student.thesis_advisor}")
        except FileNotFoundError:
            print("The input file with student info could not be found.")

    elif object_type == "Admin":
        f_name = input("First name: ")
        l_name = input("Last name: ")
        address = input("Address: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        bday = input("Birthday: ")
        salary = input("Salary: ")
        courses_taught = []
        amt = int(input("How many courses does this administrator teach: "))
        for x in range(amt):
            course_id = input("Enter the class ID: ")
            for course in read_courses().values():
                if course.course_id == course_id:
                    courses_taught.append(course)
        dep_name = input("Department name: ")
        dep = None
        for department in read_deps().values():
            if department.name == dep_name:
                dep = department
                break
        if not dep:
            print(Fore.RED + "This department does not exist. System will exit.")
            exit(1)
        new_admin = Admin(f_name, l_name, address, phone, email, bday, dep, courses_taught, salary)
        courses_taught_str = ",".join([course.course_id for course in courses_taught])
        try:
            with open(constant.ADMIN_FILE, "a") as f:
                f.write(
                    f"\nADMIN|{new_admin.first_name}|{new_admin.last_name}|{new_admin.address}|"
                    f"{new_admin.phone}|{new_admin.email}|{new_admin.birthday}|{new_admin.department.name}"
                    f"|{courses_taught_str}|{new_admin.salary}\n")
        except FileNotFoundError:
            print("The input file with student info could not be found.")
