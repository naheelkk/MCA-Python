# MCA-Python
Python Lab Programs MCA Semester 1

input_string = input("Enter a string: ")

# Extract the first character
first_char = input_string[0]

# Replace all occurrences of the first character with '$' except the first one
updated_string = first_char + input_string[1:].replace(first_char, '$')

print("Updated string:", updated_string)
