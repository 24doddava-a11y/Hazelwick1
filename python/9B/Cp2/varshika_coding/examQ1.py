count = 0
while(count < 8):
    h = float(input("Enter your height in cm: "))
    if h >= 140 :
        count = count +1
        print("You are allowed to ride.")
    elif h >= 120 :
        a = input("Are you riding with an adult? ")
        if a == "yes":
            count = count +1
            print("You are allowed to ride.")
        else:
            print("You aren't allowed to ride.")
    else:
        print("You aren't allowed to ride.")

#print("The ride is full. Please wait for the next ride .")