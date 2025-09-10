
'''Python Project: Gradebook Manager
---

Create a Python program to manage student grades using lists, tuples, and dictionaries. 
This project will give you practice with:
- Variables and data types
- Lists and dictionaries
- Loops and conditionals
- User user_input
- Calculating averages and summaries

---

Requirements
1. Create a Gradebook
- Use a dictionary where keys are student names and values are lists of grades.
- Add at least 3 students initially, each with at least 3 grades.
2. User user_input
- Allow the user to:
  - Add a new student
  - Add grades for an existing student
  - View the gradebook summary
3. Calculations
- For each student, calculate the average grade.
- Identify and print the student with the highest average.
4. Display
- Print a clear summary of all students, their grades, and their average.
- Example output:
  - Alice: [90, 85, 92] Average: 89.0
  - Bob: [78, 81, 86] Average: 81.7
  - Top Student: Alice
---
5. Additional Features (Required)
- Allow the user to remove a student or a grade.
- Display letter grades (A, B, C, etc.) based on averages.
- Sort students by average grade.
---

Rubric (40 points total)
- 10 pts: Dictionary with students and grades initialized
- 10 pts: User user_input works to add students and grades
- 10 pts: Correct calculation of averages and top student
- 10 pts: Clear display of gradebook summary
'''
gradebook = {"James": [89, 100, 83], "Jonah": [73, 62, 78], "Jeff": [98, 100, 99]}


def add_student():
    name_input = input("\nInput a name to add to the gradebook\nName: ")
    if not(name_input.lower() in gradebook.lower()):
        gradebook[name_input] = []
    else:
        print("a")

def add_grade():
    print("add grade")

def view_summary():
    print("view summary")

while True:
    user_input = input("\nWhat would you like to do?\nOptions: \"Add Student\", \"Add Grades\", \"View Summary\", or \"Exit\".\nSelect: ").lower()
    if user_input in ("add student", "add students", "student", "students"):
        add_student()
    elif user_input in ("add grade", "add grades", "grade", "grades"):
        add_grade()
    elif user_input in ("view summary", "view", "summary"):
        view_summary()
    elif user_input in ("end", "exit", "stop", "leave"):
        break
    else:
        print("User input not recognized.")