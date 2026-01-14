"""
Pornsawan Khareram
683040156-9
"""

from datetime import date

# ==================================================
# Base Class
# ==================================================
class Person:
    _running_number = 1   # for ID generation

    def __init__(self, name, age, birthdate, bloodgroup, is_married):
        self.name = name
        self.age = age
        self._birthdate = birthdate
        self._id = self.__generate_id()
        self.__bloodgroup = bloodgroup
        self.__is_married = is_married

    def __generate_id(self):
        year = date.today().year
        pid = f"{year}{Person._running_number:03d}"
        Person._running_number += 1
        return pid

    def display_public_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self._id}")


# ==================================================
# Level 2 : Staff
# ==================================================
class Staff(Person):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 department, start_year):
        super().__init__(name, age, birthdate, bloodgroup, is_married)
        self.department = department
        self.start_year = start_year
        self.tenure_year = self.__calculate_tenure_year()
        self.__salary = 0

    def __calculate_tenure_year(self):
        return date.today().year - self.start_year

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display_public_info(self):
        super().display_public_info()
        print(f"Department: {self.department}")
        print(f"Tenure Year: {self.tenure_year}")
        print(f"Salary: {self.__salary}")


# ==================================================
# Level 3 : Professor
# ==================================================
class Professor(Staff):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 department, start_year, professorship, admin_position=0):
        super().__init__(name, age, birthdate, bloodgroup, is_married,
                         department, start_year)
        self.professorship = professorship
        self.admin_position = admin_position
        self.set_salary()

    def set_salary(self):
        salary = (
            30000
            + self.tenure_year * 1000
            + self.professorship * 10000
            + self.admin_position * 10000
        )
        super().set_salary(salary)

    def display_public_info(self):
        super().display_public_info()
        print(f"Professorship Level: {self.professorship}")
        print(f"Admin Position: {self.admin_position}")


# ==================================================
# Level 3 : Administrator
# ==================================================
class Administrator(Staff):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 department, start_year, admin_position):
        super().__init__(name, age, birthdate, bloodgroup, is_married,
                         department, start_year)
        self.admin_position = admin_position
        self.set_salary()

    def set_salary(self):
        salary = (
            15000
            + self.tenure_year * 800
            + self.admin_position * 5000
        )
        super().set_salary(salary)

    def display_public_info(self):
        super().display_public_info()
        print(f"Admin Level: {self.admin_position}")


# ==================================================
# Level 2 : Student
# ==================================================
class Student(Person):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 start_year, major, level, grade_list=None):
        super().__init__(name, age, birthdate, bloodgroup, is_married)
        self.start_year = start_year
        self.major = major
        self.level = level
        self.grade_list = grade_list or []
        self.gpa = self.calculate_instance_gpa()
        self.__graduation_date = self.__calculate_graduation_date()

    @staticmethod
    def calculate_gpa(credits, grades):
        grade_map = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
        total_points = sum(c * grade_map[g] for c, g in zip(credits, grades))
        total_credits = sum(credits)
        return round(total_points / total_credits, 2) if total_credits else 0

    def calculate_instance_gpa(self):
        if not self.grade_list:
            return 0
        credits, grades = zip(*self.grade_list)
        return Student.calculate_gpa(credits, grades)

    def __calculate_graduation_date(self):
        if self.level.lower() == "undergraduate":
            return self.start_year + 4
        return self.start_year + 2

    def display_public_info(self):
        super().display_public_info()
        print(f"Major: {self.major}")
        print(f"Level: {self.level}")
        print(f"GPA: {self.gpa}")
        print(f"Graduation Year: {self.__graduation_date}")


# ==================================================
# Level 3 : UndergraduateStudent
# ==================================================
class UndergraduateStudent(Student):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 start_year, major, club=None, grade_list=None):
        super().__init__(
            name, age, birthdate, bloodgroup, is_married,
            start_year, major, "undergraduate", grade_list
        )
        self.club = club
        self.course_list = []

    def register_course(self, course):
        self.course_list.append(course)

    def display_public_info(self):
        super().display_public_info()
        print(f"Club: {self.club}")
        print(f"Courses: {self.course_list}")


# ==================================================
# Level 3 : GraduateStudent
# ==================================================
class GraduateStudent(Student):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 start_year, major, advisor_name, grade_list=None):
        self.__proposal_date = None
        super().__init__(
            name, age, birthdate, bloodgroup, is_married,
            start_year, major, "graduate", grade_list
        )
        self.advisor_name = advisor_name
        self.thesis_name = None

    def __calculate_graduation_date(self):
        if self.__proposal_date:
            return self.__proposal_date.year + 1
        return date.today().year + 2

    def set_thesis_name(self, thesis_name):
        self.thesis_name = thesis_name

    def set_proposal_date(self, proposal_date):
        self.__proposal_date = proposal_date

    def get_proposal_date(self):
        return self.__proposal_date

    def display_public_info(self):
        super().display_public_info()
        print(f"Advisor: {self.advisor_name}")
        print(f"Thesis: {self.thesis_name}")
        print(f"Proposal Date: {self.__proposal_date}")


# ==================================================
# Example Run
# ==================================================
if __name__ == "__main__":
    ug = UndergraduateStudent(
        "mei", 20, "2005-01-01", "B", False,
        2023, "IT", "Robotics",
        grade_list=[(3, "A"), (3, "B")]
    )

    gs = GraduateStudent(
        "Tee", 25, "2000-02-02", "AB", False,
        2024, "AI", "Dr. Smith"
    )
    gs.set_thesis_name("Deep Learning")
    gs.set_proposal_date(date(2025, 6, 1))

    prof = Professor(
        "Dr. Smith", 45, "1979-05-10", "O", True,
        "Computer Science", 2015, 3, 1
    )

    ug.display_public_info()
    print("-" * 30)
    gs.display_public_info()
    print("-" * 30)
    prof.display_public_info()
