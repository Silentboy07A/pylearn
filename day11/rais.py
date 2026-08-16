try:
    age = int(input("Enter the age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

    print("Age:", age)

except ValueError as e:
    print("Invalid age:", e)