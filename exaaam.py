name=input("enter the student name:- ")
pythonmark=int(input("enter the python mark:- "))
mathsmark=int(input("enter the maths mark:- "))
physicsnmark=int(input("enter the physics mark:- "))
total=pythonmark+mathsmark+physicsnmark
average=pythonmark+mathsmark+physicsnmark/3
print(pythonmark)
print(mathsmark)
print(physicsnmark)
print(total)
print(average)



if mathsmark>=35 and pythonmark>=35 and physicsnmark>=35:
    print("passed")
else:
    print("failed")





