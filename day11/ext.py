try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print(a / b)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")