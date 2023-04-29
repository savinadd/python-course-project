class Person:
    def __init__(self, first_name, last_name, address, phone, email, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = birthday

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_birthday(self):
        return self.birthday
    