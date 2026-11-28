"""
Full Name: Benedict Matthew O. Zacarias
Section: IV-BSIT-A
Activity Code: P8 - Inheritance and Polymorphism
Date: December 17, 2026
"""

# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Kumusta, ako si {self.name} at ako ay {self.age} taong gulang.")

# Child Class 1: Student (nagmamana sa Person)
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    # Method overriding
    def introduce(self):
        print(f"Ako si {self.name}, {self.age} yrs old, isang estudyante ng {self.course}.")

# Child Class 2: Teacher (nagmamana sa Person)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    # Method overriding
    def introduce(self):
        print(f"Magandang araw! Ako si Sir {self.name} ({self.age}), nagtuturo ng {self.subject}.")

def main():
    # Gumawa ng objects mula sa parent at child classes
    person1 = Person("Benedict Matthew Zacarias", 25)
    student1 = Student("Rhuella Untalan", 21, "BSIT")
    teacher1 = Teacher("Carl Ferrer", 30, "Python & Node.js")

    # Polymorphism: pagsama-samahin sa iisang list at tawagin ang introduce()
    people = [person1, student1, teacher1]

    print("--- PAGPAPAKILALA (POLYMORPHISM) ---")
    for p in people:
        p.introduce()

if __name__ == "__main__":
    main()

# Explanation: (Inheritance at Polymorphism):
# Ipinapakita ng program ang inheritance dahil ang Student at Teacher ay parehong nagmana ng mga
# katangian (name at age) at method mula sa parent class na Person gamit ang super().__init__().
# Ang polymorphism naman ay makikita nang ni-override ng Student at Teacher ang introduce() method
# upang magbigay ng magkaibang mensahe. Kahit nasa iisang listahan silang lahat, alam ng Python kung
# aling bersyon ng introduce() ang tatawagin para sa bawat object.
