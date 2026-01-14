"""
Pornsawan Khareram
683040156-9
"""
from datetime import datetime

class Person:
    def __init__(self, name, age, birthdate, bloodgroup, is_married):
        self.name = name
        self.age = age
        self._birthdate = birthdate
        self._id = self.__generate_id()
        self.__bloodgroup = bloodgroup
        self.__is_married = is_married

    def __generate_id(self):
        year = datetime.today().year
        pid = f"{year}{Person._running_number:03d}"
        Person._running_number += 1
        return pid

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self._id}")

class Staff(Person):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 department, start_year):
        super().__init__(name, age, birthdate, bloodgroup, is_married)
        self.department = department
        self.start_year = start_year
        self.tenure_year = datetime.today().year - start_year
        self.__salary = 0
        self.tenure_year = self.__calculate_tenure()

    def __calculate_tenure(self):
       return datetime.now().year - self.start_year

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):
         super().display_info()
         print(f"Department {self.department}")
         print(f"Tenure year: {self.tenure_year}")
         print(f"Salary: {self.___salary()}")


class Student(Person):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 start_year, major, level, grade_list=None):
        super().__init__(name, age, birthdate, bloodgroup, is_married)
        self.start_year = start_year
        self.major = major
        self.level = level
        self.grade_list = grade_list if grade_list else []
        self._graduation_date = None
        
    def calculate_gpa(self):
        grade_map = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
        total = 0
        total_credits = 0

        for course in self.grade_list:
            total_points += credits * grade_map[grade]
            total_credits += credits
        def calculate_gpa(self):
            return self.calculate_gpa(self.grade_list)
        
        def __calculate_graduation_date(self):
            if self.level == "undergraduate":
                return self.start_year + 4
            elif self.level == "graduate":
                return self.start_year + 2
            return None

        def display_info(self):
            super().display_info()
            print(f"Major: {self.major}")
            print(f"Level: {self.level}")
            print(f"GPA: {self.calculate_gpa()}")
            print(f"Graduation : {self.__graduation_date()}")

class Professor(Staff):
    def __init__(self, name, age, birthdate, bloodgroup, is_married, department, start_year):
        super().__init__(name, age, birthdate, bloodgroup, is_married, department, start_year)
        self.tenure_year = 1000
        self.admin_positions = []
        self.set_salary()

    def set_salary(self, salary):
        salary =(
            30000
            + self.tenure_year * 1000
            + self.Professorship * 10000
            + self.admin_position * 10000
        )
        super().set_salary(salary)

    def display_info(self):
            super().display_info()
            print(f"Professorship: {self.Professorship}")
            print(f"Admin Level: {self.admin_positions}")

class administrator(Staff):
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

    def display_info(self):
            super().display_info()
            print(f"Admin Level: {self.admin_position}")

class UndergraduateStudent(Student):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 start_year, major, level, grade_list=None, club=None, course_list=None):
        super().__init__(name, age, birthdate, bloodgroup, is_married, start_year, major, level, grade_list)
        self.club = club
        self.course_list = course_list if course_list else []
      
    def register_course(self, course):
        self.course_list.append(course)

    def display_info(self):
       super().display_info()
       print(f"Club: {self.club}")
       print(f"Courses: {self.course_list}")

class GraduateStudent(Student):
    def __init__(self, name, age, birthdate, bloodgroup, is_married,
                 start_year, major, grade_list=None, advisor_name=None):
        super().__init__(
            name, age, birthdate, bloodgroup, is_married,
            start_year, major, "graduate", grade_list
        )
        self.advisor_name = advisor_name
        self.thesis_name = None
        self._proposal_date = None
        self.student_graduation_date = None

    def _student_calculate_graduation_date(self):
        if self._proposal_date:
            return self._proposal_date.year + 1
        return datetime.today().year + 2

    def set_proposal_date(self, proposal_date):
        self._proposal_date = proposal_date
        self.student_graduation_date = self._student_calculate_graduation_date()

    def set_thesis_name(self, thesis_name):
        self.thesis_name = thesis_name

    def get_proposal_date(self):
        return self._proposal_date

    def display_info(self):
        super().display_info()
        print(f"ADVISOR : {self.advisor_name}")
        print(f"THESIS : {self.thesis_name}")
        print(f"PROPOSAL : {self._proposal_date}")



