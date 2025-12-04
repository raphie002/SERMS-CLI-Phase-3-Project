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

    new_stu = Student(name=name, age=age, department=dept)
    session.add(new_stu)
    session.commit()

    print("Student added successfully!")

def update_student():
    list_students()
    sid = int(input("\nEnter student ID to update: "))

    student = session.query(Student).get(sid)
    if not student:
        print("Student not found.")
        return

    student.name = input(f"New name ({student.name}): ") or student.name
    student.age = int(input(f"New age ({student.age}): ") or student.age)
    student.department = input(f"New department ({student.department}): ") or student.department

    session.commit()
    print("Student updated!")

def delete_student():
    list_students()
    sid = int(input("\nEnter student ID to delete: "))

    student = session.query(Student).get(sid)
    if not student:
        print("Student not found.")
        return

    session.delete(student)
    session.commit()
    print("Student deleted!")

# ---------------- PLACEHOLDER MENUS ---------------- #

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
            print("Invalid choice. Try again.")


def list_courses():
    courses = session.query(Course).all()
    print("\n--- COURSES ---")
    for c in courses:
        print(f"{c.id}. {c.name} ({c.code})")


def add_course():
    print("\n--- ADD COURSE ---")
    name = input("Course name: ")
    code = input("Course code: ")
    description = input("Description: ")

    new_course = Course(
        name=name,
        code=code,
        description=description
    )
    session.add(new_course)
    session.commit()

    print("Course added successfully!")


def update_course():
    list_courses()
    cid = int(input("\nEnter course ID to update: "))

    course = session.query(Course).get(cid)
    if not course:
        print("Course not found.")
        return

    course.name = input(f"New name ({course.name}): ") or course.name
    course.code = input(f"New code ({course.code}): ") or course.code
    course.description = input(
        f"New description ({course.description}): ") or course.description

    session.commit()
    print("Course updated!")


def delete_course():
    list_courses()
    cid = int(input("\nEnter course ID to delete: "))

    course = session.query(Course).get(cid)
    if not course:
        print("Course not found.")
        return

    session.delete(course)
    session.commit()
    print("Course deleted!")


def grade_menu():
    while True:
        print("\n--- GRADE MENU ---")
        print("1. List all grades")
        print("2. Add grade")
        print("3. Update grade")
        print("4. Delete grade")
        print("5. Back")

        choice = input("Choose an option: ")

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
        else:
            print("Invalid choice.")


def list_grades():
    grades = session.query(Grade).all()
    print("\n--- GRADES ---")
    for g in grades:
        print(f"{g.id}. {g.student.name} - {g.course.name} | Score: {g.score} | Grade: {g.letter}")


def add_grade():
    print("\n--- ADD GRADE ---")
    
    # List students
    students = session.query(Student).all()
    print("\nStudents:")
    for s in students:
        print(f"{s.id}. {s.name}")

    student_id = int(input("Enter student ID: "))

    # List courses
    courses = session.query(Course).all()
    print("\nCourses:")
    for c in courses:
        print(f"{c.id}. {c.name} ({c.code})")

    course_id = int(input("Enter course ID: "))

    score = float(input("Score: "))
    letter = input("Letter grade: ")

    new_grade = Grade(
        student_id=student_id,
        course_id=course_id,
        score=score,
        letter=letter
    )

    session.add(new_grade)
    session.commit()
    print("Grade added successfully!")


def update_grade():
    list_grades()
    gid = int(input("\nEnter grade ID to update: "))

    grade = session.query(Grade).get(gid)
    if not grade:
        print("Grade not found.")
        return

    print(f"\nUpdating grade for: {grade.student.name} in {grade.course.name}")

    score = input(f"New score ({grade.score}): ")
    letter = input(f"New letter ({grade.letter}): ")

    grade.score = float(score) if score else grade.score
    grade.letter = letter if letter else grade.letter

    session.commit()
    print("Grade updated!")


def delete_grade():
    list_grades()
    gid = int(input("\nEnter grade ID to delete: "))

    grade = session.query(Grade).get(gid)
    if not grade:
        print("Grade not found.")
        return

    session.delete(grade)
    session.commit()
    print("Grade deleted!")


def attendance_menu():
    while True:
        print("\n--- ATTENDANCE MENU ---")
        print("1. List all attendance records")
        print("2. Add attendance record")
        print("3. Update attendance record")
        print("4. Delete attendance record")
        print("5. Back")

        choice = input("Choose an option: ")

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
        else:
            print("Invalid choice.")

def list_attendance():
    records = session.query(Attendance).all()
    print("\n--- ATTENDANCE RECORDS ---")
    for a in records:
        print(f"{a.id}. {a.student.name} | {a.course.name} | {a.date} | {a.status}")


def add_attendance():
    print("\n--- ADD ATTENDANCE ---")

    # List students
    students = session.query(Student).all()
    print("\nStudents:")
    for s in students:
        print(f"{s.id}. {s.name}")
    student_id = int(input("Enter student ID: "))

    # List courses
    courses = session.query(Course).all()
    print("\nCourses:")
    for c in courses:
        print(f"{c.id}. {c.name} ({c.code})")
    course_id = int(input("Enter course ID: "))

    date = input("Enter date (YYYY-MM-DD): ")
    status = input("Status (Present / Absent / Late): ").title()

    new_record = Attendance(
        student_id=student_id,
        course_id=course_id,
        date=date,
        status=status
    )

    session.add(new_record)
    session.commit()
    print("Attendance record added!")


def update_attendance():
    list_attendance()
    aid = int(input("\nEnter attendance ID to update: "))

    record = session.query(Attendance).get(aid)
    if not record:
        print("Record not found.")
        return

    print(f"\nUpdating: {record.student.name} - {record.course.name}")

    date = input(f"New date ({record.date}): ")
    status = input(f"New status ({record.status}): ").title()

    record.date = date if date else record.date
    record.status = status if status else record.status

    session.commit()
    print("Attendance updated!")


def delete_attendance():
    list_attendance()
    aid = int(input("\nEnter attendance ID to delete: "))

    record = session.query(Attendance).get(aid)
    if not record:
        print("Record not found.")
        return

    session.delete(record)
    session.commit()
    print("Attendance record deleted!")


# ---------------- RUN CLI ---------------- #

if __name__ == "__main__":
    main_menu()
