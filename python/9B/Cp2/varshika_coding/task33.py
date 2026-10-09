import random
n1 = random.randint(0,100)
n2 = random.randint(0,100)
n3 = random.randint(0,100)
n4 = random.randint(0,100)
n5 = random.randint(0,100)
p = 0

g1 = int(input("guess the number from 0 to 100: "))

if g1 == n1:
    p = p+10
    print("bang-on")


elif g1 > (n1-5) and g1 < (n1+5):
    p = p+5
    print("close (within range of 5)")

elif g1 > (n1-10) and g1 < (n1+10):
    p = p+2
    print("okay (within range of 10)")

else:
    p = p+0
    print("way off (off by +11)")

g2 = int(input("guess the number from 0 to 100: "))

if g2 == n2:
    p = p+10
    print("bang-on")

elif g2 > (n2-5) and g2 < (n2+5):
    p = p+5
    print("close (within range of 5)")

elif g2 > (n2-10) and g2 < (n2+10):
    p = p+2
    print("okay (within range of 10)")

else:
    p = p+0
    print("way off (off by +11)")

g3 = int(input("guess the number from 0 to 100: "))

if g3 == n3:
    p = p+10
    print("bang-on")

elif g3 > (n3-5) and g3 < (n3+5):
    p = p+5
    print("close (within range of 5)")

elif g3 > (n3-10) and g3 < (n3+10):
    p = p+2
    print("okay (within range of 10)")

else:
    p = p+0
    print("way off (off by +11)")

g4 = int(input("guess the number from 0 to 100: "))

if g4 == n4:
    p = p+10
    print("bang-on")

elif g4 > (n4-5) and g4 < (n4+5):
    p = p+5
    print("close (within range of 5)")

elif g4 > (n4-10) and g4 < (n4+10):
    p = p+2
    print("okay (within range of 10)")

else:
    p = p+0
    print("way off (off by +11)")

g5 = int(input("guess the number from 0 to 100: "))

if g5 == n5:
    p = p+10
    print("bang-on")

elif g5 > (n5-5) and g5 < (n5+5):
    p = p+5
    print("close (within range of 5)")

elif g5 > (n5-10) and g5 < (n5+10):
    p = p+2
    print("okay (within range of 10)")

else:
    p = p+0
    print("way off (off by +11)")

print("you scored",p)