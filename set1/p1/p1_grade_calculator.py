
# Name: [YOUR FULL NAME]
# Section: IV-BSIT A
# Activity: P1 - Student Grade Calculator
# Date: November 15, 2026

# Function 1: Accept grades from the user
def enter_grades():
    grades = []

    # Ask how many grades the user wants to enter
    while True:
        try:
            number = int(input("How many grades will you enter? "))

            if number > 0:
                break
            else:
                print("Please enter at least one grade.")

        except ValueError:
            print("Please enter a valid whole number.")

    # Ask for each grade
    for i in range(number):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be from 0 to 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades


# Function 2: Calculate the average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function 3: Get the highest grade
def get_highest(grades):
    return max(grades)


# Function 4: Get the lowest grade
def get_lowest(grades):
    return min(grades)


# Function 5: Check if the student passed or failed
def check_result(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function 6: Display the results
def show_results(grades):
    if len(grades) == 0:
        print("Please enter grades first.")
        return

    print("\n===== STUDENT GRADE REPORT =====")
    print("Grades:", grades)
    print("Average:", round(calculate_average(grades), 2))
    print("Highest Grade:", get_highest(grades))
    print("Lowest Grade:", get_lowest(grades))
    print("Final Result:", check_result(grades))


# Main function: Display the menu
def main():
    grades = []

    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            grades = enter_grades()

        elif choice == "2":
            show_results(grades)

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# Variable Scope Explanation:
# A local variable is declared inside a function and can only be used there.
# For example, the grades variable inside enter_grades() is local.
# A global variable is declared outside all functions and can be accessed
# by different functions. This program mainly uses local variables.
