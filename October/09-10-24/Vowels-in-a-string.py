str = input("Enter a string:")
vowels = ['a','A','e','E','i','I','o','O','u','U']
temp = []

for i in str:
    if i in vowels:
        temp.append(i)

print(f"Vowels in the string {str} is {temp}")
        
