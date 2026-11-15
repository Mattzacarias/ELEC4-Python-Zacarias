# Name: Benedict Matthew Zacarias
# Section: IV-BSIT A
# Activity: P2: Custom Module: student_utils
# Date: November 15, 2026

# Kinukuha ang average ng listahan ng grades
def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

# Tinutukoy kung pasado (75 pataas) o bagsak
def determine_pass_fail(average):
    return "PASSED" if average >= 75 else "FAILED"

# Kinukuha ang pinakamataas na grade
def get_highest_grade(grades):
    return max(grades)

# Kinukuha ang pinakamababang grade
def get_lowest_grade(grades):
    return min(grades)

if __name__ == "__main__":
    # Simpleng test kapag direktang ni-run ang module na ito
    sample = [80, 85, 90]
    print("Test Average:", calculate_average(sample))
