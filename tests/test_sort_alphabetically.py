import unittest
from undergraduate import Undergraduate
from admin import Admin
from department import Department
from course import Course
from sort_alphabetically import sort_alphabetically


class TestSortAlphabetically(unittest.TestCase):
    def test_sort_admins_by_first_name(self):
        admins = {
            "admin1": Admin("John", "Doe", "123 N Vine Avenue, USA", "123456789",
                            "john@gmail.com", "04-01-1999", "COS", "COS 1020, COS 1050", "3000"),
            "admin2": Admin("Ann", "Smith", "Ul Hristo Botev 12, Sofia, Bulgaria", "12343454",
                            "ann@gmail.com", "01-01-1977", "INF", "INF 1030, INF 2080", "4000"),
            "admin3": Admin("Zane", "Adam", "Ul Nqkude 12, Bulgaria", "123456", "z@gmail.com",
                            "11-05-1988", "MAT", "MAT 1004", "5000"),
        }
        expected_order = ["admin2", "admin1", "admin3"]
        sorted_dict = sort_alphabetically(admins)
        self.assertEqual(list(sorted_dict.keys()), expected_order)

    def test_sort_courses_by_id(self):
        courses = {
            "course1": Course("Python", "COS 1111", "COS", "Savina Dimitrova", "09-2023", "04-2023", "40"),
            "course2": Course("English 101", "ENG 1001", "ENG", "Abc Def", "09-2023", "12-2023", "50"),
            "course3": Course("Finite Math", "MAT 1000", "MAT", "Petar Dalakov", "09-2024", "11-2024", "30"),
        }
        expected_order = ["course1", "course2", "course3"]
        sorted_dict = sort_alphabetically(courses)
        self.assertEqual(list(sorted_dict.keys()), expected_order)

    def test_sort_departments_by_name(self):
        departments = {
            "dept1": Department("Computer Science", "Anton Stoilov", "COS 1001, COS 1002, COS 1508"),
            "dept2": Department("Mathematics", "Math Chair", "MAT 1000, MAT 1001, MAT 1002"),
            "dept3": Department("Physics", "Physics Chair", "PHY 1000, PHY 1001, PHY 1002"),
        }
        expected_order = ["dept1", "dept2", "dept3"]
        sorted_dict = sort_alphabetically(departments)
        self.assertEqual(list(sorted_dict.keys()), expected_order)

    def test_sort_undergrads_by_first_name(self):
        undergrads = {
            "u1": Undergraduate("John", "Doe", "123 Address Street", "12346567", "john@gmail.com",
                                "07-01-1997", "4.0", "COS", "05-2025", "2", "60", "COS 1020, COS 1050"),
            "u2": Undergraduate("Yvenne", "Smith", "456 Address Street", "1239048390", "yvenne@gmail.com",
                                "11-02-2000", "3.2", "INF", "05-2024", "3", "80", "INF 1000, ENG 1000, MAT1000"),
            "u3": Undergraduate("Bob", "Johnson", "789 Address Street", "24384903840", "bob@gmail.com",
                                "03-01-2001", "2.0", "ENG", "05-2025", "3", "90", "ENG 1000, COS 1000"),
        }
        expected_order = ["u3", "u1", "u2"]
        sorted_dict = sort_alphabetically(undergrads)
        self.assertEqual(list(sorted_dict.keys()), expected_order)
