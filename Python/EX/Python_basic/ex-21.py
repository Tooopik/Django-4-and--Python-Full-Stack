def divider(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Please do not divide by zero!')
