#2. Vowel and Consonant Counter (Using Strings Only)
# Ask user to enter text
text = input("Enter a word or sentence: ")
# Convert to lowercase to simplify checks
text = text.lower()
# Initialize counters
vowel_count = 0
consonant_count = 0
# Vowel characters
vowels = "aeiou"
# Loop through each character
for char in text:
    if char >= 'a' and char <= 'z':  # Check if character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
# Print results
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)