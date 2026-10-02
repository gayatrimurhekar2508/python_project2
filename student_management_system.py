import csv
import os

FILE = "students.csv"
FIELDS = ["name", "roll_number", "marks"]

def ensure_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=FIELDS).writeheader()

def read_students():
    ensure_file()
    with open(FILE, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def save_students(students):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)

def add_student():
    students = read_students()
    student = {
        "name": input("Enter student name: ").strip(),
        "roll_number": input("Enter roll number: ").strip(),
        "marks": input("Enter marks: ").strip()
    }
    students.append(student)
    save_students(students)
    print("Student added successfully.")

def display_students():
    students = read_students()
    if not students:
        print("No student records found.")
        return
    print("\nName | Roll Number | Marks")
    print("-" * 30)
    for s in students:
        print(f"{s['name']} | {s['roll_number']} | {s['marks']}")

def search_student():
    roll = input("Enter roll number: ").strip()
    for s in read_students():
        if s["roll_number"] == roll:
            print("Student found:", s)
            return
    print("Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ").strip()
    students = read_students()
    updated = [s for s in students if s["roll_number"] != roll]
    if len(updated) == len(students):
        print("Student not found.")
    else:
        save_students(updated)
        print("Student deleted successfully.")

def update_student():
    roll = input("Enter roll number to update: ").strip()
    students = read_students()
    for s in students:
        if s["roll_number"] == roll:
            s["name"] = input("Enter new name: ").strip()
            s["marks"] = input("Enter new marks: ").strip()
            save_students(students)
            print("Student updated successfully.")
            return
    print("Student not found.")

def main():
    ensure_file()
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1": add_student()
        elif choice == "2": display_students()
        elif choice == "3": search_student()
        elif choice == "4": update_student()
        elif choice == "5": delete_student()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
