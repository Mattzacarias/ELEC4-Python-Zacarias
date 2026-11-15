# Name: Benedict Matthew Zacarias
# Section: IV-BSIT A
# Activity: P2: Custom Module: student_utils
# Date: November 15, 2026

# Unang import style: import module
import datetime
import student_utils

# Pangalawang import style: from module import name
from student_utils import calculate_average, determine_pass_fail

def main():
    grades = []
    print("--- GRADE REPORT USING CUSTOM MODULE ---")
    
    # Humingi ng 3 simpleng grade mula sa user
    for i in range(3):
        while True:
            try:
                g = float(input(f"Ilagay ang grade #{i + 1} (0-100): "))
                if 0 <= g <= 100:
                    grades.append(g)
                    break
                print("Dapat 0 hanggang 100 lang.")
            except ValueError:
                print("Numero lang ang ilagay.")

    # Paggamit ng mga function mula sa student_utils
    avg = calculate_average(grades)
    status = determine_pass_fail(avg)
    highest = student_utils.get_highest_grade(grades)
    lowest = student_utils.get_lowest_grade(grades)

    # Paggamit ng built-in datetime module para ipakita ang oras ng report
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %I:%M %p")

    print("\n--- RESULTA ---")
    print(f"Report Generated: {formatted_time}")
    print(f"Grades: {grades}")
    print(f"Average: {avg:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Status: {status}")

if __name__ == "__main__":
    main()
