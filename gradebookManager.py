
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
gradebook = {"James": [], "Jonah": [73, 62, 78], "Jeff": [98, 100, 99]}
line_break = "\n"+"-"*30+"\n"
#[89, 100, 83]

def add_student():
    print(line_break)
    while(True):
        name_input = input("Input a name to add to the gradebook or type \"Cancel\".\nName: ")
        if name_input.lower() == "cancel":
            print("\nReturning to Home.")
            return
        looped_name = False
        if name_input == "":
            print("\nCannot add blank names.\n")
            looped_name = True
        for student_name in gradebook:
            if name_input.lower() == student_name.lower():
                looped_name = True
                print(f"\nStudent named \"{name_input}\" already in gradebook.\n")
                break
        if not(looped_name):
            print(f"\nAdded student {name_input} to gradebook.")
            gradebook[name_input] = []
            return

def add_grade():
    print(line_break)
    while(True):
        name_query = input("Input a name to add a grade to (Case sensitive) or type \"Cancel\".\nName: ")
        if name_query.lower() == "cancel":
            print("\nReturning to Home.")
            return
        name_recognized = False
        for student_name in gradebook:
            if student_name == name_query:
                name_recognized = True
                while True:
                    try:
                        grade_input = (input(f"{line_break}\nInput a grade for {name_query} by entering a number between 0-100 or type \"Cancel\".\nGrade: "))
                        if grade_input.lower() == "cancel":
                            print("\nReturning to name query.\n"+line_break)
                            break
                        if int(grade_input) >= 0 and int(grade_input) <= 100:
                            gradebook[name_query].append(int(grade_input))
                            print(f"\nAdded a score of {grade_input} to student {student_name}.\n{line_break}")
                            while True:
                                add_more = input(f"Would you like to add more grades to student {name_query}?\nEnter \"Add\" or \"Cancel\".\nInput: ").lower()
                                if add_more == "add":
                                    print("\nReturning to grade query.")
                                    break
                                elif add_more == "cancel":
                                    print("\nReturning to Home.")
                                    return
                                else:
                                    print("\nInput not recognized.\n")
                        else:
                            print("Grade was over 100 or under 0.")
                    except:
                        print("Grade was not a recognizable integer.")
        if not(name_recognized):
            print("\nName not recognized.\n")

def view_summary():
    highest_grade = 0
    highest_students = []
    print(line_break+"\nGrade summary:",end="")
    for student in gradebook:
        if len(gradebook[student]) != 0:
            print(f"\n - Grades of student {student}: ",end="")
            print(*gradebook[student],sep=", ",end="")
            student_average = 0
            for grade in gradebook[student]:
                student_average+=grade/len(gradebook[student])
            if len(gradebook[student]) != 1:
                print(f" Average: {student_average:.2f}",end="")
            if student_average > highest_grade:
                highest_grade = student_average
                highest_students = [student]
            elif student_average == highest_grade:
                highest_students.append(student)
        else:
            print(f"\n - {student} has no grades.",end="")
    print("\nHighest grade belongs to ",end="")
    print(*highest_students,sep=", ",end="")
    print(f" with a grade of {highest_grade:.2f}")
    

while True:
    user_input = input(line_break+"\nWhat would you like to do?\nOptions: \"Add Student\", \"Add Grades\", \"View Summary\", or \"Exit\".\nSelect: ").lower()
    if user_input in ("add student", "add students", "student", "students"):
        add_student()
    elif user_input in ("add grade", "add grades", "grade", "grades"):
        add_grade()
    elif user_input in ("view summary", "view", "summary"):
        view_summary()
    elif user_input in ("end", "exit", "stop", "leave"):
        break
    else:
        print("\nUser input not recognized.")