# ----------------------------------Week 1 Tasks – Operators------------------------------------------------------------
# 1. BMI Calculator from User Input
# Ask user to enter body weight in kilograms
weight = float(input("Enter your weight in kg: "))
# Ask user to enter height in meters
height = float(input("Enter your height in meters: "))
# Calculate BMI using the formula: BMI = weight / (height^2)
bmi = weight / (height ** 2)
# Print the BMI rounded to 2 decimal places
print("Your BMI is:", round(bmi, 2))