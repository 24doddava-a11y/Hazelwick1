row = 1

while row <= 3:
    col = 1
    while col <= 3:
        print(col,end=" ")
        col += 1
    print()
    row += 1

for i in range(1,4):
    for j in range(1,4):
        print(i*j, end=" ")
    print()