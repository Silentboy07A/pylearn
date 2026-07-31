name = input("Enter name: ")
roll = input("Enter roll number: ")

m1 = int(input("Enter Mark 1: "))
m2 = int(input("Enter Mark 2: "))
m3 = int(input("Enter Mark 3: "))
m4 = int(input("Enter Mark 4: "))
m5 = int(input("Enter Mark 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("\n========== REPORT CARD ==========")
print("Name     :", name)
print("Roll No  :", roll)
print("Mark 1   :", m1)
print("Mark 2   :", m2)
print("Mark 3   :", m3)
print("Mark 4   :", m4)
print("Mark 5   :", m5)
print("-------------------------------")
print("Total    :", total)
print("Average  :", average)
print("================================")