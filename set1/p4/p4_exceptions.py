# Name: Benedict Matthew Zacarias
# Section: IV-BSIT A
# Activity: P4 - Safe Menu Program
# Date: November 16, 2026

# Function para sa division na may ValueError at ZeroDivisionError handling
def safe_divide():
    try:
        num1 = float(input("Ilagay ang unang numero: "))
        num2 = float(input("Ilagay ang pangalawang numero: "))
        result = num1 / num2
    except ValueError:
        print("Error (ValueError): Numero lamang ang dapat ilagay!")
    except ZeroDivisionError:
        print("Error (ZeroDivisionError): Hindi pwedeng mag-divide sa zero!")
    else:
        # Tatakbo lang ito kapag walang naganap na error
        print(f"Sagot: {num1} / {num2} = {result}")
    finally:
        # Laging tatakbo may error man o wala
        print("Tapos na ang division operation.")

# Function para magbukas ng file na may FileNotFoundError handling
def safe_open_file():
    filename = input("Ilagay ang pangalan ng file (hal. sample.txt): ").strip()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error (FileNotFoundError): Hindi mahanap ang file na '{filename}'.")
    else:
        print("\n--- LAMAN NG FILE ---")
        print(content)
    finally:
        print("Tapos na ang pagbasa ng file.")

def main():
    while True:
        print("\n--- SAFE MENU PROGRAM ---")
        print("1. Divide Two Numbers")
        print("2. Open and Read a File")
        print("3. Exit")
        choice = input("Pumili (1-3): ").strip()

        if choice == "1":
            safe_divide()
        elif choice == "2":
            safe_open_file()
        elif choice == "3":
            print("Salamat! Ligtas na isinara ang program.")
            break
        else:
            print("Invalid menu choice! Pumili lamang ng 1, 2, o 3.")

if __name__ == "__main__":
    main()
