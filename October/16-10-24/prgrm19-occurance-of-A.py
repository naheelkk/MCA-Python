names_list = [] 
counted = []
size = int(input("Enter size: "))  

for i in range(size):
    item = str(input(f"Enter Name {i + 1}: "))
    names_list.append(item)


total_a_count = 0 

for name in names_list:
    if name not in counted:
        a_count = name.count('a')  
        caps_a_count = name.count('A') 
        total_a_count += (a_count + caps_a_count) 
        counted.append(name)  

print(f"Total occurrences of 'a' and 'A': {total_a_count}")
print(counted)
