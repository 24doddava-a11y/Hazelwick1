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