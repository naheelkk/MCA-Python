current_year = 2024
end_year = int(input(f'Complete the range of years From {current_year} to ?'))
years_in_between = []
leap_years = []
for year in range(current_year, end_year + 1):
    if(year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)):
        leap_years.append(year)

print(leap_years)
