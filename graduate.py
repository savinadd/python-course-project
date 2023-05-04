from student import Student
from colorama import Fore, Style


class Graduate(Student):
    """
      A class to represent an graduate student.

      ...

      Attributes
      ----------
      f_name : str
      first name of the admin
      l_name : str
      last name of the admin
      address : str
      address of admin
      phone : str
      phone number
      email : str
      email of admin
      birthday : str
      birthday of admin
      thesis topic : str
      topic that the graduate will be presenting a thesis on
      thesis advisor : Admin
      the administrator overlooking the thesis project

      """
    def __init__(self, first_name, last_name, address, phone, email, birthday, gpa,
                 thesis_topic, thesis_advisor):
        super().__init__(first_name, last_name, address, phone, email, birthday, gpa)
        self.thesis_topic = thesis_topic
        self.thesis_advisor = thesis_advisor

    def __str__(self):
        return f"{super().__str__()}{Fore.LIGHTMAGENTA_EX}\nThesis topic: {self.thesis_topic}\nThesis Advisor: " \
               f"{self.thesis_advisor.first_name} {self.thesis_advisor.last_name} {Style.RESET_ALL}\n"
