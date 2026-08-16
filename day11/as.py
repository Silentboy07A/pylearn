try:
    n = int(input("Enter a number"))
except ValueError:
    print("Enter a valid number")
else:
    print("Square is =",n**2)
    