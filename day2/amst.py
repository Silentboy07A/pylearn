n=int(input("Enter a no"))
o=n
s=0
while n>0:
    digit=n%10
    s=s+digit**3
    n=n//10
if s==o:
    print("Armstrong")
else:
    print("Not Armstrong")