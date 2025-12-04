# lib/seed.py
import random
from datetime import date, timedelta

from lib.database import session
from lib.models import Student, Instructor, Course, Grade, Attendance


# 1. CLEAR TABLES (safe for development)
def clear_tables():
    session.query(Attendance).delete()
    session.query(Grade).delete()
    session.query(Student).delete()
    session.query(Instructor).delete()
    session.query(Course).delete()
    session.commit()
    print("✔ Tables cleared")


# 2. SEED HELPERS
def create_students():
    students = [
        Student(name="John Mwangi", age=20, department="Computer Science"),
        Student(name="Alice Wanjiku", age=22, department="Mathematics"),
        Student(name="Brian Otieno", age=19, department="Engineering"),
        Student(name="Sarah Njeri", age=21, department="Computer Science"),
    ]
    session.add_all(students)
    session.commit()
    print("✔ Students added")
    return students


def create_instructors():
    instructors = [
        Instructor(name="Dr. Kamau", department="Computer Science"),
        Instructor(name="Prof. Achieng", department="Mathematics"),
        Instructor(name="Dr. Kiptoo", department="Engineering"),
    ]
    session.add_all(instructors)
    session.commit()
    print("✔ Instructors added")
    return instructors


def create_courses():
    courses = [
        Course(name="Advanced Calculus", code="MA202", description="Second year calculus."),
        Course(name="Data Structures", code="CS102", description="Introduction to DS."),
        Course(name="Thermodynamics", code="EN105", description="Basic Engineering Thermodynamics."),
        Course(name="Discrete Mathematics", code="CS110", description="Logic and proofs."),
    ]
    session.add_all(courses)
    session.commit()
    print("✔ Courses added")
    return courses


# 3. RANDOM GRADE GENERATOR
def generate_letter(score: float):
    if score >= 80: return "A"
    if score >= 70: return "B"
    if score >= 60: return "C"
    if score >= 50: return "D"
    return "F"


def create_grades(students, courses):
    grade_entries = []

    for student in students:
        for course in courses:
            score = random.uniform(40, 95)
            letter = generate_letter(score)

            grade_entries.append(
                Grade(
                    student_id=student.id,
                    course_id=course.id,
                    score=round(score, 2),
                    letter=letter
                )
            )

    session.add_all(grade_entries)
    session.commit()
    print("✔ Grades generated")


# 4. RANDOM ATTENDANCE GENERATOR
def create_attendance(students, courses):
    attendance_entries = []
    start_date = date(2025, 1, 1)

    # Generate 20 days of attendance
    for day_offset in range(20):
        current = start_date + timedelta(days=day_offset)

        for student in students:
            for course in courses:
                status = random.choice(["Present", "Absent", "Late"])

                attendance_entries.append(
                    Attendance(
                        student_id=student.id,
                        course_id=course.id,
                        date=current,
                        status=status
                    )
                )

    session.add_all(attendance_entries)
    session.commit()
    print("✔ Attendance generated")


# 5. RUN SEEDING
if __name__ == "__main__":
    clear_tables()

    students = create_students()
    instructors = create_instructors()
    courses = create_courses()

    create_grades(students, courses)
    create_attendance(students, courses)

    print("\n🌱 Database seeding completed successfully!\n")
