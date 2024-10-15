num1 = int(input("Enter 1st number:"))

num2 = int(input("Enter 2nd number:"))

num3 = int(input("Enter 3rd number:"))

if num1>num2 and num1>num3:
    print(f"{num1} is largest number!!")
elif num2>num1 and num2>num3:
    print(f"{num2} is largest number!!")
else:
    print(f"{num3} is he largest number!!")
