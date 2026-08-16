
try:
    n = int(input("Enter a number: "))
    print(n ** 2)
except ValueError:
    print("Invalid number")
else:
    print("Calculation successful")
finally:
    print("Program finished")