# Simple Student Result Management System (Console)

students = []  # Empty list to store student data

# Function to add a student
def add_student():
    name = input("Enter student's name: ")
    roll = input("Enter roll number: ")
    try:
        marks1 = float(input("Enter marks in Subject 1: "))
        marks2 = float(input("Enter marks in Subject 2: "))
        marks3 = float(input("Enter marks in Subject 3: "))
    except ValueError:
        print("❌ Please enter valid marks!")
        return

    total = marks1 + marks2 + marks3
    percentage = total / 3

    # Grade logic
    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 75:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 40:
        grade = 'C'
    else:
        grade = 'F'

    # Save all data in a dictionary
    student = {
        "name": name,
        "roll": roll,
        "marks": [marks1, marks2, marks3],
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)
    print("✅ Student record added successfully!\n")

# Function to view all student records
def view_students():
    if not students:
        print("No student records yet.")
        return

    print("\n===== Student Records =====")
    for s in students:
        print(f"Name: {s['name']}")
        print(f"Roll No: {s['roll']}")
        print(f"Marks: {s['marks']}")
        print(f"Total: {s['total']}")
        print(f"Percentage: {s['percentage']:.2f}%")
        print(f"Grade: {s['grade']}")
        print("------------------------")

# Main menu loop
while True:
    print("\n==== Student Result Management System ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        print("Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please select 1, 2, or 3.")
