 #1. Grade Calculator (Using Strings and Conditions)
# Ask the user to enter marks
marks = float(input("Enter your marks (0–100): "))
# Use conditions to assign grades
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"
# Show grade
print("Your grade is:", grade)