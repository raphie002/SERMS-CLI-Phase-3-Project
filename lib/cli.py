# lib/cli.py
from lib.database import session
from lib.models import Student, Course, Grade, Attendance
import sys


def main_menu():
    while True:
        print("\n=== SCHOOL MANAGEMENT SYSTEM ===")
        print("1. Students")
        print("2. Courses")
        print("3. Grades")
        print("4. Attendance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            grade_menu()
        elif choice == "4":
            attendance_menu()
        elif choice == "5":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")


# ---------------- STUDENT MENU ---------------- #

def student_menu():
    while True:
        print("\n--- STUDENT MENU ---")
        print("1. List students")
        print("2. Add student")
        print("3. Update student")
        print("4. Delete student")
        print("5. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            list_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def list_students():
    students = session.query(Student).all()
    print("\n--- STUDENTS ---")
    for s in students:
        print(f"{s.id}. {s.name} ({s.department})")


def add_student():
    print("\n--- ADD STUDENT ---")
    name = input("Name: ")
    age = int(input("Age: "))
    dept = input("Department: ")

    session.add(Student(name=name, age=age, department=dept))
    session.commit()
    print("✔ Student added")


def update_student():
    list_students()
    sid = int(input("\nEnter student ID to update: "))

    student = session.query(Student).filter(Student.id == sid).first()
    if not student:
        print("Student not found.")
        return

    student.name = input(f"New name ({student.name}): ") or student.name
    student.age = int(input(f"New age ({student.age}): ") or student.age)
    student.department = input(f"New department ({student.department}): ") or student.department

    session.commit()
    print("✔ Student updated")


def delete_student():
    list_students()
    sid = int(input("\nEnter ID to delete: "))

    student = session.query(Student).filter(Student.id == sid).first()
    if not student:
        print("Not found.")
        return

    session.delete(student)
    session.commit()
    print("✔ Student deleted")


# ---------------- COURSE MENU ---------------- #

def course_menu():
    while True:
        print("\n--- COURSE MENU ---")
        print("1. List courses")
        print("2. Add course")
        print("3. Update course")
        print("4. Delete course")
        print("5. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            list_courses()
        elif choice == "2":
            add_course()
        elif choice == "3":
            update_course()
        elif choice == "4":
            delete_course()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def list_courses():
    courses = session.query(Course).all()
    print("\n--- COURSES ---")
    for c in courses:
        print(f"{c.id}. {c.name} ({c.code})")


def add_course():
    print("\n--- ADD COURSE ---")
    name = input("Name: ")
    code = input("Code: ")
    desc = input("Description: ")

    session.add(Course(name=name, code=code, description=desc))
    session.commit()
    print("✔ Course added")


def update_course():
    list_courses()
    cid = int(input("\nEnter ID to update: "))

    course = session.query(Course).filter(Course.id == cid).first()
    if not course:
        print("Not found.")
        return

    course.name = input(f"New name ({course.name}): ") or course.name
    course.code = input(f"New code ({course.code}): ") or course.code
    course.description = input(f"New description: ") or course.description

    session.commit()
    print("✔ Course updated")


def delete_course():
    list_courses()
    cid = int(input("\nEnter ID to delete: "))

    course = session.query(Course).filter(Course.id == cid).first()
    if not course:
        print("Not found.")
        return

    session.delete(course)
    session.commit()
    print("✔ Course deleted")


# ---------------- GRADE MENU ---------------- #

def grade_menu():
    while True:
        print("\n--- GRADE MENU ---")
        print("1. List grades")
        print("2. Add grade")
        print("3. Update grade")
        print("4. Delete grade")
        print("5. Back")

        choice = input("Choose: ")

        if choice == "1":
            list_grades()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            update_grade()
        elif choice == "4":
            delete_grade()
        elif choice == "5":
            break


def list_grades():
    grades = session.query(Grade).all()
    print("\n--- GRADES ---")
    for g in grades:
        print(f"{g.id}. {g.student.name} - {g.course.name} | {g.score} | {g.letter}")


def add_grade():
    print("\n--- ADD GRADE ---")
    students = session.query(Student).all()
    courses = session.query(Course).all()

    for s in students:
        print(f"{s.id}. {s.name}")
    student_id = int(input("Student ID: "))

    for c in courses:
        print(f"{c.id}. {c.name}")
    course_id = int(input("Course ID: "))

    score = float(input("Score: "))
    letter = input("Letter: ").upper()

    session.add(Grade(student_id=student_id, course_id=course_id, score=score, letter=letter))
    session.commit()
    print("✔ Grade added")


def update_grade():
    list_grades()
    gid = int(input("\nEnter ID to update: "))

    grade = session.query(Grade).filter(Grade.id == gid).first()
    if not grade:
        print("Not found.")
        return

    new_score = input(f"New score ({grade.score}): ")
    new_letter = input(f"New letter ({grade.letter}): ").upper()

    if new_score: grade.score = float(new_score)
    if new_letter: grade.letter = new_letter

    session.commit()
    print("✔ Grade updated")


def delete_grade():
    list_grades()
    gid = int(input("\nEnter ID to delete: "))

    grade = session.query(Grade).filter(Grade.id == gid).first()
    if not grade:
        print("Not found.")
        return

    session.delete(grade)
    session.commit()
    print("✔ Grade deleted")


# ---------------- ATTENDANCE MENU ---------------- #

def attendance_menu():
    while True:
        print("\n--- ATTENDANCE MENU ---")
        print("1. List records")
        print("2. Add record")
        print("3. Update record")
        print("4. Delete record")
        print("5. Back")

        choice = input("Choose: ")

        if choice == "1":
            list_attendance()
        elif choice == "2":
            add_attendance()
        elif choice == "3":
            update_attendance()
        elif choice == "4":
            delete_attendance()
        elif choice == "5":
            break


def list_attendance():
    records = session.query(Attendance).all()
    print("\n--- ATTENDANCE ---")
    for a in records:
        print(f"{a.id}. {a.student.name} | {a.course.name} | {a.date} | {a.status}")


def add_attendance():
    students = session.query(Student).all()
    courses = session.query(Course).all()

    print("\nStudents:")
    for s in students: print(f"{s.id}. {s.name}")
    sid = int(input("Student ID: "))

    print("\nCourses:")
    for c in courses: print(f"{c.id}. {c.name}")
    cid = int(input("Course ID: "))

    date_str = input("Date (YYYY-MM-DD): ")
    status = input("Status (Present/Absent/Late): ").title()

    session.add(Attendance(student_id=sid, course_id=cid, date=date_str, status=status))
    session.commit()
    print("✔ Attendance added")


def update_attendance():
    list_attendance()
    aid = int(input("\nEnter ID to update: "))

    record = session.query(Attendance).filter(Attendance.id == aid).first()
    if not record:
        print("Not found.")
        return

    new_date = input(f"New date ({record.date}): ")
    new_status = input(f"New status ({record.status}): ").title()

    if new_date: record.date = new_date
    if new_status: record.status = new_status

    session.commit()
    print("✔ Attendance updated")


def delete_attendance():
    list_attendance()
    aid = int(input("\nEnter ID to delete: "))

    record = session.query(Attendance).filter(Attendance.id == aid).first()
    if not record:
        print("Not found.")
        return

    session.delete(record)
    session.commit()
    print("✔ Attendance deleted")


if __name__ == "__main__":
    main_menu()
