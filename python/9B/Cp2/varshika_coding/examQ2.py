a = int(input("Enter the number of hours you have parked for: "))
while(a == 0):
    cost = a * 4
    car = input("Is your car electric? ")
    if car == "yes":
        cost = cost / 2
        print("£",cost)
    else:
        print("£",cost)