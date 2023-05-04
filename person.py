from colorama import Fore, Style


class Person:
    """
      A class to represent a person.

      ...

      Attributes
      ----------
      f_name : str
      first name of the person
      l_name : str
      last name of the person
      address : str
      address of person
      phone : str
      phone number
      email : str
      email of person
      birthday : str
      birthday of person

      """
    def __init__(self, first_name, last_name, address, phone, email, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = birthday

    def __str__(self):
        return f"{Fore.YELLOW}{self.first_name} {self.last_name}{Style.RESET_ALL}, " \
               f"\nAddress: {self.address}, Phone: {self.phone}, Email: {self.email}, Birthday: {self.birthday}"
