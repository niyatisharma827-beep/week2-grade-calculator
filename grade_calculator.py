"""
Student Grade Calculator
Week 2 Project - Control Flow & Data Structures
Author: Niyati Sharma
"""

def calculate_grade(average):
    """Calculate grade and feedback comment based on average marks."""
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', "Very Good! You're doing well."
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'


def get_valid_number(prompt, min_val=0, max_val=100):
    """Prompt user for a valid float number within [min_val, max_val]."""
    while True:
        try:
            val = float(input(prompt))
            if min_val <= val <= max_val:
                return val
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_positive_int(prompt):
    """Prompt user for a positive non-zero integer."""
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def main():
    print("=" * 50)
    print("           STUDENT GRADE CALCULATOR")
    print("=" * 50)
    print()

    # Get number of students
    num_students = get_positive_int("Enter number of students: ")

    student_names = []
    student_marks = []
    student_results = []

    # Collect data for each student
    for i in range(num_students):
        print(f"\n=== STUDENT {i + 1} ===")
        
        while True:
            name = input("Student name: ").strip()
            if name != "":
                break
            print("Name cannot be empty!")
        student_names.append(name)

        print("Enter marks (0-100):")
        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")

        student_marks.append([math, science, english])

        # Calculate average and grade
        average = (math + science + english) / 3.0
        grade, comment = calculate_grade(average)

        student_results.append({
            'average': average,
            'grade': grade,
            'comment': comment
        })

    # Display Results Summary Table
    print("\n" + "=" * 65)
    print("                         RESULTS SUMMARY")
    print("=" * 65)
    print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | {'Comment'}")
    print("-" * 65)

    for i in range(num_students):
        name = student_names[i]
        avg = student_results[i]['average']
        grade = student_results[i]['grade']
        comment = student_results[i]['comment']
        print(f"{name:<20} | {avg:>5.1f} | {grade:^5} | {comment}")

    # Calculate and display class statistics
    if num_students > 0:
        averages = [res['average'] for res in student_results]
        class_avg = sum(averages) / len(averages)
        
        max_avg = max(averages)
        min_avg = min(averages)
        
        max_index = averages.index(max_avg)
        min_index = averages.index(min_avg)

        print("\n" + "=" * 50)
        print("                 CLASS STATISTICS")
        print("=" * 50)
        print(f"Total Students: {num_students}")
        print(f"Class Average: {class_avg:.1f}")
        print(f"Highest Average: {max_avg:.1f} ({student_names[max_index]})")
        print(f"Lowest Average: {min_avg:.1f} ({student_names[min_index]})")

    print("\n" + "=" * 50)
    print("Thank you for using the Grade Calculator!")
    print("=" * 50)


if __name__ == "__main__":
    main()