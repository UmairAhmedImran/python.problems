def calculate_grades(n):
    if n >= 0 and n < 50:
        print("Your grade is F.")
    elif n >= 50 and n < 65:
        print("Your grade is P.")
    elif n >= 65 and n < 75:
        print("Your grade is C.")
    elif n >= 75 and n < 85:
        print("Your grade is D.")
    elif n >= 85 and n < 100:
        print("Your grade is HD.")
    else:
        print("Invalid input")