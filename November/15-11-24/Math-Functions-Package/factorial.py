def factorial(sankya):
    if sankya == 1 or sankya == 0:
        return 1
    else:
        return (sankya * factorial(sankya - 1))
