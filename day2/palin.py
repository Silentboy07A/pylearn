n=int(input("Enter a no"))
rev=0
o= n
while n>0:

    digit =n%10
    rev=rev*10+digit
    n=n//10
if rev==o:
    print("Palindrome")
else:
    print("Not palindrome")
