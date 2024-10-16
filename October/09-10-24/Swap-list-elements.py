lst = [36,51,3,12,89,510]
length = len(lst)
print(f"List before swapping:{lst}")

temp = lst[0]
lst[0] = lst[length-1]
lst[length-1] = temp

print(f"List after swapping:{lst}")
