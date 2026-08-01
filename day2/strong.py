n = int(input("Enter a number"))

o = n
s = 0

while n > 0:
    digit = n % 10

    fact = 1

    for i in range(1, digit + 1):
        fact *= i

    s += fact
    n //= 10

if o == s:
    print("Strong Number")
else:
    print("Not Strong Number")