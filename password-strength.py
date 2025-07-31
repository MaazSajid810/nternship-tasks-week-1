#2. Password Strength Classifier (Using String Logic Only)
# Ask the user to enter a password
password = input("Enter your password: ")
# Initialize flags
has_upper = False
has_lower = False
has_digit = False
has_special = False
# Define special characters
special_characters = "!@#$%^&*()-_+=<>?/|"
# Check each character in password
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_special = True
# Check password strength based on criteria
if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    strength = "Strong"
elif len(password) >= 6 and (has_upper or has_lower) and (has_digit or has_special):
    strength = "Medium"
else:
    strength = "Weak"
# Display result
print("Password strength:", strength)