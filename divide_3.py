#2. Sum of Numbers Divisible by 3 (Up to a Limit)
# Ask the user to enter an upper limit
limit = int(input("Enter the upper limit: "))
# Initialize sum
sum_divisible_by_3 = 0
# Loop through numbers from 1 to limit
for i in range(1, limit + 1):
    if i % 3 == 0:
        sum_divisible_by_3 += i
# Display result
print("Sum of numbers divisible by 3 up to", limit, "is:", sum_divisible_by_3)