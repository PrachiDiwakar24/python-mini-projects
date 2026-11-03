#  Student Management System 


students = []

def add_student():

    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "Roll No": roll,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    print("Student Added Successfully!")


def view_students():

    if not students:
        print("No Student Records Found!")
    else:
        for student in students:
            print("----------------------")
            print("Roll No:", student["Roll No"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])


def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["Roll No"] == roll:
            print("Student Found!")
            print(student)
            return

    print("Student Not Found!")


def update_student():
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student["Roll No"] == roll:
            student["Name"] = input("Enter New Name: ")
            student["Age"] = input("Enter New Age: ")
            student["Course"] = input("Enter New Course: ")
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["Roll No"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Try Again.")






