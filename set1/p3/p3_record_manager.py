# Name: Benedict Matthew Zacarias
# Section: IV-BSIT A
# Activity: P3 - Student Record Manager
# Date: November 16, 2026

# Nagdadagdag ng bagong estudyante at pinipigilan ang duplicate
def add_student(students_list, seen_lower):
    name = input("Ilagay ang buong pangalan ng estudyante: ").strip()
    if not name:
        print("Hindi pwedeng blangko ang pangalan.")
        return

    # Ginagawang lowercase para pantay ang check (hal. Juan Cruz == juan cruz)
    if name.lower() in seen_lower:
        print(f"Mayroon nang '{name}' sa listahan. Hindi na idinagdag.")
    else:
        students_list.append(name)
        seen_lower.add(name.lower())
        print(f"Naidagdag si '{name}'.")

# Nagtatanggal ng estudyante sa listahan at set
def remove_student(students_list, seen_lower):
    name = input("Ilagay ang pangalang tatanggalin: ").strip()
    for s in students_list:
        if s.lower() == name.lower():
            students_list.remove(s)
            seen_lower.remove(s.lower())
            print(f"Natanggal si '{s}'.")
            return
    print("Hindi mahanap ang pangalang iyan.")

# Naghahanap ng estudyante kahit bahagi lang ng pangalan (partial search)
def search_student(students_list):
    keyword = input("Ilagay ang hahanaping pangalan: ").strip().lower()
    matches = [s for s in students_list if keyword in s.lower()]
    if matches:
        print("Mga nahanap na estudyante:")
        for m in matches:
            print(f"- {m}")
    else:
        print("Walang tumugmang estudyante.")

# Nagpapakita ng lahat ng estudyante nang naka-alphabetical order
def display_students(students_list):
    if not students_list:
        print("Walang laman ang listahan.")
        return
    sorted_names = sorted(students_list, key=str.lower)
    print(f"\n--- LISTAHAN NG MGA ESTUDYANTE (Total: {len(sorted_names)}) ---")
    for idx, student in enumerate(sorted_names, start=1):
        print(f"{idx}. {student}")

def main():
    students_list = []     # List para itago ang eksaktong format ng pangalan
    seen_lower = set()     # Set para mabilis na ma-check kung may duplicate na

    while True:
        print("\n--- STUDENT RECORD MANAGER ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")
        choice = input("Pumili (1-5): ")

        if choice == "1":
            add_student(students_list, seen_lower)
        elif choice == "2":
            remove_student(students_list, seen_lower)
        elif choice == "3":
            search_student(students_list)
        elif choice == "4":
            display_students(students_list)
        elif choice == "5":
            print("Salamat! Paalam.")
            break
        else:
            print("Maling pili. Pumili mula 1 hanggang 5.")

if __name__ == "__main__":
    main()

# Paliwanag (List vs Set):
# Ang list ay isang ordered collection na pwedeng maglaman ng magkakaparehong items at madaling i-sort,
# kaya ginamit ko ito sa 'students_list' upang maipakita ang mga pangalan nang naka-alphabetical order.
# Ang set naman ay isang unordered collection na hindi tumatanggap ng duplicate values at mabilis mag-check
# kung may kapareho na. Ginamit ko ang set na 'seen_lower' upang itago ang lowercase na bersyon ng mga pangalan
# at agad mapigilan ang pag-uulit ng entry.
