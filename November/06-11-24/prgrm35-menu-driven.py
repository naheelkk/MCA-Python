# Create a menu driven program to read a list of n numbers from the user 
# and do the following
# 1.find the greatest and lowest number
# 2.sort list in ascending order
# 3.create another list of even numbers
#----------------------------------------------------------------------------#
size = int(input("Enter Size of your list"))
lst = []
print('Enter elements')

for i in range(size):
    ele = int(input())
    lst.append(ele);

user_input = int(input("Enter Choice From 1 - 3 "))

def Switch(self,user_input,lst):
    if user_input == 1:
        return max(lst), min(lst)
    elif user_input == 2:
        return lst.sort()
    elif user_input == 3:
        return even_number_list(size)
    # elif user_input == 4:
    else:
        return 'Wrong Choice'

def even_number_list(size):
    lst = []
    for i in range(size):
        if i % 2 != 0:
            continue
        else:
            lst.append(i)
