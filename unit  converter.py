def convert_length():
    print("\nLength Conversion:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371
        print(f"{km} km = {round(miles, 2)} miles")
    elif choice == "2":
        miles = float(input("Enter miles: "))
        km = miles / 0.621371
        print(f"{miles} miles = {round(km, 2)} km")
    else:
        print("Invalid choice.")
def convert_weight():
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        kg = float(input("Enter kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kg = {round(pounds, 2)} lbs")
    elif choice == "2":
        pounds = float(input("Enter pounds: "))
        kg = pounds / 2.20462
        print(f"{pounds} lbs = {round(kg, 2)} kg")
    else:
        print("Invalid choice.")
def convert_temperature():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {round(f, 2)}°F")
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {round(c, 2)}°C")
    else:
        print("Invalid choice.")
# Main loop
while True:
    print("\n--- Unit Converter ---")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")
    main_choice = input("Select conversion type (1-4): ")
    if main_choice == "1":
        convert_length()
    elif main_choice == "2":
        convert_weight()
    elif main_choice == "3":
        convert_temperature()
    elif main_choice == "4":
        print("Exiting Unit Converter. Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")
