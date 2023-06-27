import grade_calculator

total_marks = int(input("Enter total marks: "))
total_subjects = int(input("Enter number of subjects: "))

avg = total_marks/total_subjects

grade_calculator.calculate_grades(avg)