count = 0
while count <= 4:
    import random
    n = random.randint(0,100)
    p = 0

    g = int(input("guess the number from 0 to 100: "))

    if g == n:
        p = p+10
        print("bang-on")

    elif g > (n-5) and g < (n+5):
        p = p+5
        print("close (within range of 5)")

    elif g > (n-10) and g < (n+10):
        p = p+2
        print("okay (within range of 10)")

    else:
        p = p+0
        print("way off (off by +11)")
    count+=1