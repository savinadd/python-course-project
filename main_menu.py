from file_read_deps import read_deps
from file_read_courses import read_courses
from file_read_admins import read_admin
from file_read_students import read_students
from sort_alphabetically import sort_alphabetically
from colorama import Fore, Style
from write_to_file import write_to_file


def return_menu():
    """
          This method allows for better user interaction with the program
          and has been separated to minimize code repetition.
    """
    choice = int(input(Fore.GREEN + "\nEnter 1 to return to the main menu, enter 2 to exit:   " + Style.RESET_ALL))
    if choice == 1:
        menu()
    if choice == 2:
        print(Fore.RED + Style.BRIGHT + "Thank you for using the university management system! Goodbye!")
        exit(1)
    else:
        print(Fore.RED + "Invalid number entered. The program will exit. Thank you!")
        exit(1)


def menu():
    """
           Creates a menu for the program which calls various other functions
           based on user input.
    """
    print("𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃")
    print("\n")
    print(Fore.BLUE + "Welcome to the Blagoevgrad University management system!")
    print(Style.RESET_ALL + "\n")
    print("𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃𓂃")
    print("\t\t\t\t\t\tMain Menu\t\t")
    print("\t\t\t\t\t_________________")
    print("1. \t\t View the Administrator list and information\n"
          "2. \t\t View the Courses list and information\n"
          "3. \t\t View all Students and their information\n"
          "4. \t\t View all of the Departments and their information\n"
          "5. \t\t Sort a chosen item\n"
          "6. \t\t Add a new item\n")
    choice = int(input(Fore.RED + "Input the number corresponding to the choice you would like: " + Style.RESET_ALL))

    if choice == 1:
        print("\n")
        admin = read_admin()
        for x in admin.values():
            print(x.__str__())
            print("\n")
        print("Would you like to view the details of a specific administrator?")
        choice = int(input(Fore.GREEN + "Enter 1 to view the details of a specific admin, "
                           "enter 2 if you would not like to:  " + Style.RESET_ALL))
        if choice == 1:
            f_name = input("Enter the first name of the admin who's information you would like to see: ")
            l_name = input("Enter the last name of the admin who's information you would like to see: ")
            f_name = f_name.capitalize()
            l_name = l_name.capitalize()
            for x in admin.values():
                if f_name == x.first_name and l_name == x.last_name:
                    print(Fore.MAGENTA + Style.BRIGHT + "\nHere is your desired information: \n")
                    print(x.__str__())
                    return_menu()
            else:
                print(Fore.RED + "\nThe admin you would like to inspect does not exist." + Style.RESET_ALL)
                return_menu()

        if choice == 2:
            return_menu()

        else:
            print(Fore.RED + "Invalid number entered. The program will exit. Thank you!")
            exit(1)

    elif choice == 2:
        courses = read_courses()
        for x in courses.values():
            print(x.__str__())
        print("Would you like to view the details of a specific course?")
        choice = int(input(Fore.GREEN+ "Enter 1 to view the details of a specific course, "
                           "enter 2 if you would not like to:  " + Style.RESET_ALL))
        if choice == 1:
            course = input("Enter the course ID of the course you would like to inspect: ")
            for x in courses.values():
                if course == x.course_id:
                    print(Fore.MAGENTA + Style.BRIGHT + "\nHere is your desired information: \n")
                    print(x.__str__())
                    return_menu()
            else:
                print(Fore.RED + "\nThe course you would like to inspect does not exist." + Style.RESET_ALL)
                return_menu()
        if choice == 2:
            return_menu()

        else:
            print(Fore.RED + "Invalid number entered. The program will exit. Thank you!")
            exit(1)
    elif choice == 3:
        print(Fore.RED + "\n\nThis is the list of all students. Graduate students' thesis topics and "
              "advisors are highlighted in magenta for easier viewing.\n\n")
        students = read_students()
        for x in students.values():
            print(x.__str__())
        print("Would you like to view the details of a specific course?")
        choice = int(input(Fore.GREEN + "Enter 1 to view the details of a specific student, "
                           "enter 2 if you would not like to:  " + Style.RESET_ALL))
        if choice == 1:
            name = input("Enter the first and last name separated by a space of the student you would "
                         "like to inspect: ")
            for x in students.values():
                if name == x.first_name + " " + x.last_name:
                    print(Fore.MAGENTA + Style.BRIGHT + "\nHere is your desired information: \n" + Style.RESET_ALL)
                    print(x.__str__())
                    return_menu()
            else:
                print(Fore.RED + "\nThe student you would like to inspect does not exist." + Style.RESET_ALL)
                return_menu()

        if choice == 2:
            return_menu()

        else:
            print(Fore.RED + "Invalid number entered. The program will exit. Thank you!")
            exit(1)

    elif choice == 4:
        dep = read_deps()
        for x in dep.values():
            print(x.__str__())
        print("Would you like to view the details of a specific department?")
        choice = int(input(Fore.GREEN + "Enter 1 to view the details of a specific department, "
                           "enter 2 if you would not like to:  " + Style.RESET_ALL))
        if choice == 1:
            dep_choice = input("Enter the department abbreviation/name of the department you would like to inspect: ")
            for x in dep.values():
                if dep_choice == x.name:
                    print(Fore.MAGENTA + Style.BRIGHT + "\nHere is your desired information: \n")
                    print(x.__str__())
                    return_menu()
            else:
                print(Fore.RED + "\nThe department you would like to inspect does not exist." + Style.RESET_ALL)
                return_menu()

        if choice == 2:
            return_menu()

        else:
            print(Fore.RED + "Invalid number entered. The program will exit. Thank you!")
            exit(1)

    elif choice == 5:
        students = read_students()
        admins = read_admin()
        courses = read_courses()
        print(Fore.MAGENTA + "\nThis option will sort any type of item alphabetically, "
                             "for easier finding of information.\n" + Style.RESET_ALL)
        print("What would you like to sort?")
        choice = input("Your options are Students, Courses, or Administrators. Enter in your choice here: ")
        print("\n")
        if choice == "Students" or choice == "Student" or choice == "students" or choice == "student":
            sort_alphabetically(students)
        elif choice == "Courses" or choice == "Course" or choice == "courses" or choice == "course":
            sort_alphabetically(courses)
        elif choice == "Administrators" or choice == "administrators" or choice == "Admin" or choice == "admin":
            sort_alphabetically(admins)
        else:
            print(Fore.RED + "Invalid number entered. The program will exit. Thank you!")
            exit(1)
        print("\nTo view a specific item or person, please re-enter the menu "
              "and choose the from the first 3 options on the menu.")
        return_menu()

    elif choice == 6:
        print("\n")
        choice_item = input("What type of item would you like to add? "
                            "Your choices are Administrator ot student: ")
        if choice_item == "Student" or choice_item == "student":
            print("There are two types of students - Graduate and Undergraduate.")
            choice = input("What type of student would you like to add?: ")
        elif choice_item == "Administrator" or choice_item == "administrator" or \
                choice_item == "admin" or choice_item == "Admin":
            choice = "Admin"
        else:
            print(Fore.RED + "Invalid choice entered. The program will exit. Thank you!")
            exit(1)
        write_to_file(choice)
        print("\nAdded successfully.")
        return_menu()

    else:
        print(Fore.RED + "Invalid number entered. The program will exit. Thank you!")
        exit(1)
