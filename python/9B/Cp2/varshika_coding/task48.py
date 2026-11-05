row = 1
r = int(input("Enter the number of rows the triangle should be: "))
while row <= r:
    col = 1
    while col <= 3:
        print("*",end=" ")
        col += 1
    print()
    row += 1
