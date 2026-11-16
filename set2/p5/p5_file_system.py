"""
Full Name: [Your Full Name]
Section: [IV-BSIT A/B/C]
Activity Code: P5 - Student Information File System
Date: December 2026
"""

import os

# Kinukuha ang path ng students.txt sa kaparehong folder ng script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "students.txt")

# Binabasa ang records mula sa students.txt pagbukas ng program
def load_records():
    records = []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 4:
                        records.append({
                            "id": parts[0],
                            "name": parts[1],
                            "section": parts[2],
                            "average": float(parts[3])
                        })
    except FileNotFoundError:
        # Kung wala pang file, magsisimula sa walang lamang listahan
        print("Walang nakitang students.txt. Gagawa ng bago kapag nag-save.")
    return records

# Sine-save ang lahat ng records pabalik sa students.txt
def save_records(records):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        for r in records:
            file.write(f"{r['id']}|{r['name']}|{r['section']}|{r['average']}\n")

# Nagdadagdag ng bagong student record
def add_student(records):
    student_id = input("Student ID: ").strip()
    for r in records:
        if r["id"] == student_id:
            print("Mayroon nang ganyang Student ID!")
            return

    name = input("Full Name: ").strip()
    section = input("Course/Section: ").strip()
    try:
        avg = float(input("General Average: "))
    except ValueError:
        print("Invalid input! Dapat numero ang General Average.")
        return

    records.append({"id": student_id, "name": name, "section": section, "average": avg})
    save_records(records)
    print("Matagumpay na nai-save ang record!")

# Nagpapakita ng lahat ng student records
def display_all(records):
    if not records:
        print("Walang nakatalang record.")
        return
    print("\n--- STUDENT RECORDS ---")
    for r in records:
        print(f"ID: {r['id']} | Name: {r['name']} | Section: {r['section']} | Avg: {r['average']}")

# Naghahanap gamit ang Student ID
def search_by_id(records):
    target_id = input("Ilagay ang hahanaping Student ID: ").strip()
    for r in records:
        if r["id"] == target_id:
            print(f"Nahanap -> ID: {r['id']} | Name: {r['name']} | Section: {r['section']} | Avg: {r['average']}")
            return
    print("Hindi mahanap ang Student ID.")

# Nag-a-update ng impormasyon ng estudyante
def update_student(records):
    target_id = input("Ilagay ang Student ID na ia-update: ").strip()
    for r in records:
        if r["id"] == target_id:
            print(f"Kasalukuyang pangalan: {r['name']}")
            new_name = input("Bagong Full Name: ").strip()
            new_section = input("Bagong Course/Section: ").strip()
            try:
                new_avg = float(input("Bagong General Average: "))
            except ValueError:
                print("Invalid input! Hindi na-update dahil hindi numero ang average.")
                return

            r["name"] = new_name
            r["section"] = new_section
            r["average"] = new_avg
            save_records(records)
            print("Matagumpay na na-update ang record!")
            return
    print("Hindi mahanap ang Student ID.")

def main():
    records = load_records()
    while True:
        print("\n--- STUDENT INFORMATION FILE SYSTEM ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search by ID")
        print("4. Update Student")
        print("5. Exit")
        choice = input("Pumili (1-5): ").strip()

        if choice == "1":
            add_student(records)
        elif choice == "2":
            display_all(records)
        elif choice == "3":
            search_by_id(records)
        elif choice == "4":
            update_student(records)
        elif choice == "5":
            print("Salamat! Paalam.")
            break
        else:
            print("Maling pili. Subukan ulit.")

if __name__ == "__main__":
    main()
