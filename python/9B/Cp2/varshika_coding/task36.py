import random
n = random.randint(0,100)
g = int(input("guess the number from 1-100: "))
while n != g:
    if n == g:
        print("you are correct")
    elif g < n:
        print("too low")
        g = int(input("guess the number from 1-100: "))
    else:
        print("too high")
        g = int(input("guess the number from 1-100: "))
