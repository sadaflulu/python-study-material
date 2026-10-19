#11
# number=int(input("enter the num:-"))
# if number>=0:
#     print("positive number")
# elif number==0:
#     print("num is zero")
# elif number<=0:
#     print("negative number")
# #12
# mark=int(input("enter the mark:-"))
# if mark>=90 and mark<=100:
#     print("grade A")
# elif mark>=75 and mark<=89:
#     print("grade B")
# elif mark>=50 and mark<=74:
#     print("grade C")
# else:
#     print("grade D")
#13
# number1=int(input("enter the num 1:- "))
# number2=int(input("enter the num 2:- "))
# number3=int(input("enter the num 3:- "))
# if number1>=number2:
#     print("number 1 is larger number ")
# elif number2>=number3:
#     print("number 2 is larger")
# else:
#     print("number 3 is greater")
#14
# month=(input("enter the month:-").lower())
# if month in["jan","mar","may","july","aug","sep","dec" ]:
#     print("31 days")
# elif month=="feb":
#     print("28 days")
# elif month in["april","june","oct","nov"]:
#     print("30 days")
# else:
#     print("invalid")
#15
num1=int(input("enter the num:- "))
num2=int(input("enter the num:- "))
ab=input("enter the operator(+,-,*,/):-")
if ab == "+":
    print('result-',num1+num2)
elif ab == "-":
    print('result-',num1-num2)
elif ab == "*":
    print('result-',num1*num2)
elif ab=="/" and num2 != 0:
    print("result-",num1/num2)
elif ab=="/" and num2 == 0:
    print("error divisible by zero")   
    
else:
   print("invalid operator")


