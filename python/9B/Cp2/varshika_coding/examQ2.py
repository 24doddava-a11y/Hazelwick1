
while(a == 0):
    h = int(input("Enter the number of hours you have parked for: "))
    cost = h * 4
    car = input("Is your car electric? ")
    if car == "yes":
        cost = cost / 2
        print("£",cost)
    else:
        print("£",cost)