A = 0
B = 0
C = 0
ran = 0
while(True):
    v = input("vote A, B or C ")
    if v == "a" or v == "A":
        A = A + 1
    elif v == "b" or v == "B":
        B = B + 1
    elif v == "c" or v == "C":
        C = C + 1
    elif v == "end" or v =="END":
        print("A =",A)
        print("B =",B)
        print("C =",C)
        break
    else:
        ran = ran + 1