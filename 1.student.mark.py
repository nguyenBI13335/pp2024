

def input_num_students():
    return int(input("Enter the number of students: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth (DOB): ")
    return {'id': student_id, 'name': name, 'dob': dob}

def input_num_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return {'id': course_id, 'name': name}

def input_student_marks(students, course_name):
    marks = {}
    print(f"Enter marks for students in course {course_name}:")
    for student in students: 
        mark = float(input(f"Enter marks for {student['name']}: "))
        marks[student['name']] = mark
    return marks

def list_courses(courses):
    print("List of Courses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Name: {course['name']}")

def list_students(students):
    print("List of Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")

def show_student_marks(marks, course_name):
    print(f"Marks for students in course {course_name}:")
    for student, mark in marks.items(): 
        print(f"{student}: {mark}")

def main():
    students = []
    courses = []
    num_students = input_num_students()
    for _ in range(num_students):
        student_info = input_student_info()
        students.append(student_info)

    num_courses = input_num_courses()
    for _ in range(num_courses):
        course_info = input_course_info()
        courses.append(course_info)

    while True:
        print("\nMenu:")
        print("1. Input marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_courses(courses)
            course_name = input("Enter course name to input marks for: ")
            course_students_marks = input_student_marks(students, course_name)

        elif choice == '2':
            list_courses(courses)

        elif choice == '3':
            list_students(students)

        elif choice == '4':
            list_courses(courses)
            course_name = input("Enter course name to show student marks for: ")
            show_student_marks({}, course_name)

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
