num = int(input("Enter the number:"))

if num%2 == 0 and num != 0:
    print(f"{num} is an even number!")

elif num%2 == 1 and num != 0:
    print(f"{num} is an odd number!")

else:
    print("The given number is a zero!!!")
