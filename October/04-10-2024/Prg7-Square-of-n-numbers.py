n = int(input("Enter range of natural numbers you want to get squares of"))
print(f'n is {n}')
for i in range(1 , n+1):
    sq = i * i;
    print(f'{i}^2 = {sq}')