"""
# Grade Calculator Exercise

## Problem
You're building a grade calculator for a teacher who needs to calculate final grades for students. The teacher needs to:

1. Calculate the average of multiple test scores
2. Apply a curve (add points to boost grades)
3. Convert numerical grades to letter grades
4. Format the output nicely

## Requirements
Without using functions, you would need to repeat the same calculations for each student. Your task is to:

1. Create functions that eliminate code repetition
2. Make the main program easy to read and understand
3. Handle the grade calculations for multiple students

## Expected Behavior
The program should ask for student names and their test scores, then display:
- Student name
- Original average
- Curved average
- Letter grade

## Sample Run
```
Enter student name (or 'done' to finish): Alice
Enter test scores separated by spaces: 85 92 78 88
Student: Alice
Original Average: 85.8
Curved Average: 90.8 (+5 curve)
Letter Grade: A-

Enter student name (or 'done' to finish): Bob
Enter test scores separated by spaces: 72 68 75 70
Student: Bob
Original Average: 71.2
Curved Average: 76.2 (+5 curve)
Letter Grade: B-

Enter student name (or 'done' to finish): done
```

## Hints
Think about what code you would repeat for each student and turn those into functions:
- Calculating averages
- Applying curves
- Converting to letter grades
- Formatting output
"""


def calculate_grades(input):
    grades = input.split()
    grades_int = []
    for grade in grades:
        grades_int.append(int(grade))
    print(input)
    print(grades)
    print(grades_int)
    return grades_int


def avg_grades(input):
    avg = sum(input) / len(input)
    print(f"Grades Average: {avg}")
    return avg


def grade_letter(input):
    grade_in_letters = ""
    if input >= 90:
        grade_in_letters = "A"
    elif input < 90 and input >= 85:
        grade_in_letters = "B+"
    elif input < 90 and input >= 80:
        grade_in_letters = "B"
    elif input < 80 and input >= 55:
        grade_in_letters = "C"
    else:
        grade_in_letters = "F"
    print(f"Grade in Letters:{grade_in_letters}")
    return grade_in_letters


def curved_average(input):
    new_average = input + 5
    print(f"Curved Average: {new_average} ('+5 curve')")


while True:
    name = input("Enter student name or 'done' to finish: ")
    if name == "done":
        break
    grades = input("Enter student grades with space to sperate:")
    grades_int = calculate_grades(grades)
    print(f"Student: {name}")
    avg = avg_grades(grades_int)
    grade_letter(avg)
    curved_average(avg)
