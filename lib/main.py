# lib/main.py
from lib.database import SessionLocal
from lib.models import Student


def menu():
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")


def add_student(session):
    print("\n--- Add New Student ---")
    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip()

    if not age.isdigit():
        print("Age must be a number!")
        return

    student = Student(name=name, age=int(age), course=course)
    session.add(student)
    session.commit()
    print(f"Student '{name}' added successfully!")


def view_students(session):
    print("\n--- All Students ---")
    students = session.query(Student).all()

    if not students:
        print("No students found.")
        return

    for s in students:
        print(f"ID: {s.id} | Name: {s.name} | Age: {s.age} | Course: {s.course}")


def update_student(session):
    print("\n--- Update Student ---")
    student_id = input("Enter student ID to update: ")

    if not student_id.isdigit():
        print("Invalid ID!")
        return

    student = session.query(Student).filter_by(id=int(student_id)).first()

    if not student:
        print("Student not found!")
        return

    print(f"Updating: {student.name} (Leave blank to keep current value)")

    new_name = input(f"New name ({student.name}): ").strip()
    new_age = input(f"New age ({student.age}): ").strip()
    new_course = input(f"New course ({student.course}): ").strip()

    if new_name:
        student.name = new_name
    if new_age.isdigit():
        student.age = int(new_age)
    if new_course:
        student.course = new_course

    session.commit()
    print("Student updated successfully!")


def delete_student(session):
    print("\n--- Delete Student ---")
    student_id = input("Enter student ID to delete: ")

    if not student_id.isdigit():
        print("Invalid ID!")
        return

    student = session.query(Student).filter_by(id=int(student_id)).first()

    if not student:
        print("Student not found!")
        return

    confirm = input(f"Are you sure you want to delete '{student.name}'? (y/n): ").lower()
    if confirm == "y":
        session.delete(student)
        session.commit()
        print("Student deleted successfully!")
    else:
        print("Delete cancelled.")


def main():
    session = SessionLocal()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_student(session)
        elif choice == "2":
            view_students(session)
        elif choice == "3":
            update_student(session)
        elif choice == "4":
            delete_student(session)
        elif choice == "5":
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
