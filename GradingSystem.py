# Student Grade Cacluator demonstrating file handling, lists, and dictionaries
import os
import json


students = []  # list of students


def load_students():
    """Load existing students from a JSON file if it exists."""
    global students
    try:
        if os.path.exists("students.json"):
            with open("studnts.json", "r") as file:
                students = json.load(file)
                print(f"Loaded {len(students)} existing students from file.")
        else:
            print("No existing student data found. Starting fresh.")
    except Exception as e:
        print(f"Error loading students: {e}")
        students = []


def save_students():
    """Save the current list of students to a JSON file."""
    try:
        with open("students.json", "w") as file:
            json.dump(students, file, indent=2)
        print(f"Saved {len(students)} students to file.")
    except Exception as e:
        print(f"Error saving students: {e}")


def get_valid_score(prompt):
    """Get a valid score input from the user."""
    while True:
        try:
            score = int(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Enter a valid number.")


def get_student_info():
    """Get information for multiple students."""
    num_students = get_valid_number("How many students do you want to enter? ")

    for i in range(num_students):

        student = {}  # dictionary of each student for the list
        name = input(f"Enter the name of student {i + 1}: ")
        student['name'] = name

        scores = []  # list of 3 scores to append to students
        for j in range(3):
            score = int(input(f"Enter score {j + 1} for {name}: "))
            scores.append(score)

        student["scores"] = scores
        students.append(student)
        print(f"Added {name} Successfully!")


def get_valid_number(prompt):
    """Get a valid number from user"""
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("Number has to be greater than 0.")
        except ValueError:
            print("Enter a valid number.")


def calculate_grades():
    """ Calculate the average and grade for each student."""
    for student in students:
        scores = student["scores"]
        total = sum(scores)
        average = total / len(scores)

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        student["average"] = round(average, 1)
        student["grade"] = grade


def print_report():
    """Print the report of all students."""
    if not students:
        print("No students to report.")
        return
    print("\n" + "=" * 40)
    print("Student Grades Report")
    print("=" * 40)

    total_class_average = 0
    for student in students:
        print(f"Student: {student["name"]}")
        print(f"Scores: {student["scores"]}")
        print(f"Average: {student["average"]}")
        print(f"Grade: {student["grade"]}")
        print("-" * 20)
        total_class_average += student["average"]

    class_average = total_class_average / len(students)
    print(f"Class Average: {round(class_average, 1)}")

    top_student = max(students, key=lambda s: s["average"])
    print(f"Top Student: {top_student["name"]} ({top_student["average"]})")
    print("=" * 40)


def delete_student():
    """Delete a student from the list."""
    if not students:
        print("No students in the system to delete.")
        return
    print("\nCurrent students.")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student["name"]}")
    try:
        choice = int(
            input("\nEnter the number of students to delete (0 to cancel): "))

        if choice == 0:
            print("Delete canceled.")
        elif 1 <= choice <= len(students):
            delete_student = students.pop(choice - 1)
            print(
                f"Successfully deleted {delete_student["name"]} from the system.")
        else:
            print("Invalid student number.")
    except ValueError:
        print("Enter a valid number.")


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 30)
    print("\nMENU")
    print("=" * 30)
    print("1. View all students")
    print("2. Add new students")
    print("3. Delete student")
    print("4. Save and Exit")
    print("5. Quit without saving")


def main():
    """Main program loop."""
    print("Welcome to the Student Grade Calculator!")

    load_students()
    while True:
        show_menu()

        try:
            choice = input("\nEnter your choice (1-5): ")

            if choice == "1":
                calculate_grades()
                print_report()
            elif choice == "2":
                get_student_info()
                print("Students added successfully!")
            elif choice == "3":
                delete_student()
            elif choice == "4":
                calculate_grades()
                save_students()
                print("Students saved successfully! Exiting...")
                break
            elif choice == "5":
                print("Exiting without saving, Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except KeyboardInterrupt:
            print("\nExiting program.")
            break


if __name__ == "__main__":
    main()
