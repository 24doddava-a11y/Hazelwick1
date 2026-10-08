t = int(input("Enter the temperature in celsius: "))
if t < 0:
    print("Freezing")
elif t <= 20:
    print("Cold")
elif t <= 30:
    print("Warm")
elif t > 30:
    print("Hot")