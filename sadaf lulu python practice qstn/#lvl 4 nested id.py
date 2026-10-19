# #16
# username=input("enter the user name:-")
# if username=="admin":
#     password=input("enter the password:-")
#     if password=="1234":
#         print("login succefully")
#     else:
#         print("incorrect password")
# else:
#     print("username is incorrect")
#17
# examregister=input("Are you registered for exam(yes or no):-")
# if examregister=="yes":
#     id=input("do u have id ,(yes or no):-")
#     if id=="yes":
#         print("allow entry")
#     else:
#         print("don't allow entry")
# else:
#     print("register yoour exam")
#18
# age=int(input ("enter the age:-"))
# if age>=18:
#     liscence=input("do u pass driving test(yes or no):-")
#     if liscence=="yes":
#         print("eligible for driving liscence")
#     else:
#         print("apply for driving test")
# else:
#     print("not eligible for driving liscence")
#19
# discount_amount=float(input("enter the discount amount:-"))
# if discount_amount>=5000:   
#     customermembership=input("do you have membership(yes or no):-")
#     if customermembership=="yes":
#         print(discount_amount*0.1)
#     else:
#         print("take customer membership for discount")
# else:
#     print("the amount is not greater than 5000")
#20
ctlab=input("do you want to access computer lab,(yes or no):- ")
staff_student=input("are u student or staff from here?(yes or no):-")
if ctlab=="yes"and staff_student=="yes":
    valid_id=input("do you have valid id card(yes or no):-")
    if valid_id=="yes":
        print("you can access the computer lab")
    else:
        print("you need a valid id")
else:
    print("if you need to access computer lab you want to be a staff or student")




    