#----------------------------------Week 1 Tasks – Strings-------------------------------------------------------
#1.Username builder from full name.
# Ask the user to enter their full name
full_name = input("Enter your full name: ")
# Split the full name into parts (first, middle, last etc.)
name_parts = full_name.strip().lower().split()
# Build a username using first letter of first name and full last name
# Example: "John David Smith" → jsmith
if len(name_parts) >= 2:
    username = name_parts[0][0] + name_parts[-1]
else:
    username = name_parts[0]  
# If only one name, use it as username
# Display the username
print("Suggested username:", username)