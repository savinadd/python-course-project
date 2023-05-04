from colorama import Fore, Style


class Person:
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
