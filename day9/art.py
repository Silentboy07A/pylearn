def find_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(find_sum(5, 10, 15, 20))