# Name: Verdis Moorer
# Course: CSD-325
# Assignment: Module 8 - JSON Student List
# Date: September 20, 2026
# Description: This program loads student information from a JSON file,
# displays the original student list, adds a new student, displays the
# updated list, and saves the updated information back to the JSON file.

import json


def print_students(student_list):
    """Print each student's information from the student list."""
    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , "
            f"Email = {student['Email']}"
        )


# Load the student.json file into a Python list.
with open("student.json", "r") as student_file:
    students = json.load(student_file)


# Display the original student list.
print("\nThis is the original Student list.")
print_students(students)


# Create and append a new student.
new_student = {
    "F_Name": "Verdis",
    "L_Name": "Moorer",
    "Student_ID": 42601,
    "Email": "verdis.kianna@gmail.com"
}

students.append(new_student)


# Display the updated student list.
print("\nThis is the updated Student list.")
print_students(students)


# Save the updated list back to student.json.
with open("student.json", "w") as student_file:
    json.dump(students, student_file, indent=4)


print("\nThe student.json file was updated.")

