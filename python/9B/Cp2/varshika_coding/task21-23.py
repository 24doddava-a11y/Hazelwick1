def CheckAnswer(inputEnter , expected):
    if inputEnter == expected:
        print("you are correct")
        return True
    else:
        print("you are not correct. Try again.")
        return False

correctAns = 0
myArray = [1, 2, 3, 4, 5]

answers = [["20 + 10 = ", "30", "Addition"], ["20 - 10 = ", "10"],["20 * 10 = ", "200"], ["20 / 10 = ", "2"], ["200 / 10 = ", "20"]] 
for val in answers:
    print("Type of Question=", val[2])
    q1 = input(val[0])
    
    if(CheckAnswer(q1, val[1])):
        correctAns = correctAns + 1


print("correct = ", correctAns, "Out of ", len(answers))
percentage = (correctAns * 100) / len(answers) 

print("your percentage is", percentage,"%")





answers = [["20 + 10 = ", "30"], ["20 - 10 = ", "10"],["20 * 10 = ", "200"], ["20 / 10 = ", "2"]] 
for val in answers:
    while(True):
        q1 = input(val[0])
        if(CheckAnswer(q1, val[1])):
            break;
       
correctAns = 0
wrongAns = 0
answers = [["20 + 10 = ", "30"], ["20 - 10 = ", "10"],["20 * 10 = ", "200"], ["20 / 10 = ", "2"], ["200 / 10 = ", "20"]] 
for val in answers:
    q1 = input(val[0])
    if(CheckAnswer(q1, val[1])):
        correctAns = correctAns + 1
    else:
        wrongAns = wrongAns + 1

print("correct = ", correctAns, "Wrong = ", wrongAns)
percentage = (correctAns * 100) / (correctAns + wrongAns)
print("your percentage is", percentage,"%")







while(True):
    q2 = input("18 - 13 = ")
    if q2 == "5":
        print("you are correct")
        break
    else:
        print("you are not correct.")

q3 = input("25 * 16 = ")
if q3 == 400:
    print("you are correct")
else:
    print("you are not correct.")

q4 = input("365 / 358 = ")
if q2 == 1.019553073:
    print("you are correct")
else:
    print("you are not correct.")