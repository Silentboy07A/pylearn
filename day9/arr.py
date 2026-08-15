def add_all(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add_all(10, 20, 30))