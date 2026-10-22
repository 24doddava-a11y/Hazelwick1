while(True):
    t = int(input("Enter the number of hours you have parked for: "))
    c = t * 4
    if t == 0:
        break
    car = input("Is your car electric? ")
    if car == "yes":
        c = c / 2
        print("£",c)
    else:
        print("£",c)

hours = -1
total = 0
while hours > 0:
    hours = int(input("Enter the number of hours you have parked for: "))
    car = input("Is your car electric? ")
    if car == "yes":
        total = hours * 2
    else:
        total = hours * 4
    print("£",total)