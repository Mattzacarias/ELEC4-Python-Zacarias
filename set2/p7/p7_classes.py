"""
Full Name: [Your Full Name]
Section: [IV-BSIT A/B/C]
Activity Code: P7 - Student Management System with Classes
Date: December 2026
"""

# Class 1: Subject
class Subject:
    def __init__(self, code, title):
        self.code = code
        self.title = title

    def get_info(self):
        return f"{self.code} - {self.title}"

# Class 2: Student (may private attribute na __grade)
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.__grade = 0
        self.set_grade(grade)  # Gamitin ang setter para ma-validate agad

    # Getter para basahin ang private grade
    def get_grade(self):
        return self.__grade

    # Setter para palitan ang private grade na may validation
    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print(f"Invalid grade ({new_grade}) para kay {self.name}. Dapat 0-100 lang.")

    # Method para i-update ang pangalan ng estudyante
    def update_name(self, new_name):
        self.name = new_name

    # Method para ipakita ang detalye ng estudyante
    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Grade: {self.__grade}")

# Class 3: Section (nagsasama ng Subject at maraming Student objects)
class Section:
    def __init__(self, section_name, subject):
        self.section_name = section_name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        print(f"\n=== Section: {self.section_name} | Subject: {self.subject.get_info()} ===")
        for s in self.students:
            s.display_info()

def main():
    # Gumawa ng Subject object
    subj = Subject("ELEC 4", "Python Programming")

    # Gumawa ng 3 Student objects
    s1 = Student("2023-101", "Juan Cruz", 88)
    s2 = Student("2023-102", "Maria Clara", 92)
    s3 = Student("2023-103", "Jose Rizal", 85)

    # Gumawa ng Section object at ilagay ang mga estudyante
    sec = Section("IV-BSIT A", subj)
    sec.add_student(s1)
    sec.add_student(s2)
    sec.add_student(s3)

    # Ipakita ang unang listahan
    sec.list_students()

    # I-update ang isa sa mga estudyante at subukan ang invalid grade
    print("\n--- Pag-update kay Student 1 ---")
    s1.update_name("Juan Dela Cruz")
    s1.set_grade(105)  # Dapat tanggihan dahil lampas sa 100
    s1.set_grade(95)   # Tatanggapin dahil valid

    # Ipakita ulit ang lahat ng estudyante
    sec.list_students()

if __name__ == "__main__":
    main()
