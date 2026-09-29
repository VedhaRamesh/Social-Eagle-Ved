try:
    mark = float(input("Enter your mark (0-100): "))
except ValueError:
    print("Invalid input. Please enter a number between 0 and 100.")
else:
    if not 0 <= mark <= 100:
        print("Invalid mark. The mark must be between 0 and 100.")
    else:
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "E"

        print(f"Mark: {mark:g} -> Grade: {grade}")