type = input("Enter a type of maths (addition, subtraction, multiplication, division): ")
x = float(input("Enter a number: "))
y = float(input("Enter a number: "))
if type == "addition":
    print(x + y)
elif type == "subtraction":
    print(x - y)
elif type == "multiplication":
    print(x * y)
elif type == "division":
    print(x / y)
