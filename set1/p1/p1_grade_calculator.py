# Name: Benedict Matthew Zacarias
# Section: IV-BSIT A
# Activity: P1 - Student Grade Calculator
# Date: November 15, 2026

# Global variable para sa passing grade
PASSING_GRADE = 75

# Function para kunin ang mga grade mula sa user
def input_grades():
    grades = []  # Local variable na listahan ng grades
    while True:
        try:
            count = int(input("Ilang grades ang ilalagay? "))
            if count <= 0:
                print("Dapat mas mataas sa 0 ang bilang.")
                continue
            break
        except ValueError:
            print("Invalid input! Maglagay ng tamang numero.")

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Ilagay ang grade #{i + 1} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Invalid! Ang grade ay dapat nasa pagitan ng 0 at 100.")
            except ValueError:
                print("Invalid input! Numero lamang ang ilagay.")
    return grades

# Function para kunin ang average (walang print sa loob)
def get_average(grades):
    return sum(grades) / len(grades)

# Function para kunin ang pinakamataas na grade
def get_highest(grades):
    return max(grades)

# Function para kunin ang pinakamababang grade
def get_lowest(grades):
    return min(grades)

# Function para malaman kung Passed o Failed
def get_status(average, passing=PASSING_GRADE):
    if average >= passing:
        return "PASSED"
    return "FAILED"

# Main menu ng program
def main():
    student_grades = []
    while True:
        print("\n--- STUDENT GRADE CALCULATOR ---")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")
        choice = input("Pumili (1-3): ")

        if choice == "1":
            student_grades = input_grades()
            print("Matagumpay na nai-save ang mga grade!")
        elif choice == "2":
            if not student_grades:
                print("Wala pang nakalagay na grade. Piliin muna ang 1.")
            else:
                avg = get_average(student_grades)
                high = get_highest(student_grades)
                low = get_lowest(student_grades)
                status = get_status(average=avg)
                print(f"\nGrades: {student_grades}")
                print(f"Average: {avg:.2f}")
                print(f"Highest Grade: {high}")
                print(f"Lowest Grade: {low}")
                print(f"Status: {status}")
        elif choice == "3":
            print("Salamat! Paalam.")
            break
        else:
            print("Maling pili. Subukan ulit.")

if __name__ == "__main__":
    main()

# Paliwanag (Local vs Global Variable):
# Ang global variable ay idinedeklara sa labas ng mga function at pwedeng gamitin kahit saan sa program,
# tulad ng PASSING_GRADE = 75 sa itaas. Ang local variable naman ay ginagawa sa loob lamang ng isang
# function at doon lang din pwedeng gamitin, gaya ng 'grades' sa loob ng input_grades() at 'avg' sa
# loob ng main(). Hindi maaaring tawagin nang direkta ang 'avg' sa labas ng main() function.
