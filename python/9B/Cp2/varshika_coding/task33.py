import random
n = random.randint(0,100)
s = 100
t = 0
while(True):
    t = t+1
    g = int(input("guess the number from 0 to 100: "))

    if g == n:
        s = s - 0
        print("bang-on")
        print("score =",s)
        print("tries =",t)
        break

    elif g > (n-5) and g < (n+5):
        s = s - 2
        print("close")
        print("score =",s)
        print("tries =",t)

    elif g > (n-10) and g < (n+10):
        s = s - 5
        print("okay")
        print("score =",s)
        print("tries =",t)

    else:
        s = s - 10
        print("way off")
        print("score =",s)
        print("tries =",t)

    if s <= 0:
        print("you lose")
        print(n)
        break