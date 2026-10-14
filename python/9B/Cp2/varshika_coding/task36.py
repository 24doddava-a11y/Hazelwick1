import random
n = random.randint(0,100)

while(True):
    g = int(input("guess the number from 1-100: "))
    if n == g:
        print("you are correct")
        break
    elif g < n:
        print("too low")
    else:
        print("too high")