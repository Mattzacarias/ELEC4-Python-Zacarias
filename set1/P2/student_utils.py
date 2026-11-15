
# Name: Benedict Matthew Zacarias
# Section: IV-BSIT A
# Activity: P2 - Custom Module
# Date: November 15, 2026

# Function 1: Calculate the average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function 2: Check if the student passed or failed
def check_pass_fail(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function 3: Get the highest grade
def get_highest(grades):
    return max(grades)


# Function 4: Get the lowest grade
def get_lowest(grades):
    return min(grades)
