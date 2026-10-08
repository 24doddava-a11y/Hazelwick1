l1 = int(input("Enter length 1: "))
l2 = int(input("Enter length 2: "))
l3 = int(input("Enter length 3: "))
if l1 == l2 and l1 == l3:
    print("The triangle is equalateral")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")