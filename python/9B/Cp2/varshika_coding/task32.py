n = int(input("Enter a number: "))
if n % 3 == 0:
    print(n,"is divisible by 3")
if n % 5 == 0:
    print(n,"is divisible by 5")
if n % 7 == 0:
    print(n,"is divisible by 7")
else:
    print(n,"isn't divisible by 3, 5 or 7")