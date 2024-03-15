class Student:

    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"




class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}"


class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            student = Student(student_id, name, dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(course_id, name)
            self.courses.append(course)

    def input_student_marks(self):
        course_id = input("Enter the ID of the course to input marks: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            print(f"Enter marks for course {course.name}:")
            for student in self.students:
                mark = float(input(f"Enter mark for {student.name}: "))
                self.marks[(student.student_id, course.course_id)] = mark
            print("Marks input successful.")
        else:
            print("Course not found.")

    def list_courses(self):
        print("List of Courses:")
        for course in self.courses:
            print(course)

    def list_students(self):
        print("List of Students:")
        for student in self.students:
            print(student)

    def show_student_marks(self):
        course_id = input("Enter the ID of the course to show marks: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            print(f"Student marks for course {course.name}:")
            for student in self.students:
                mark = self.marks.get((student.student_id, course.course_id), "N/A")
                print(f"Student: {student.name}, Mark: {mark}")
        else:
            print("Course not found.")


def main():
    manager = StudentMarkManagement()

    while True:
        print("\n1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a course")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.input_students()
        elif choice == '2':
            manager.input_courses()
        elif choice == '3':
            manager.input_student_marks()
        elif choice == '4':
            manager.list_courses()
        elif choice == '5':
            manager.list_students()
        elif choice == '6':
            manager.show_student_marks()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
