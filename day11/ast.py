try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age")
else:
    print("Your age is", age)