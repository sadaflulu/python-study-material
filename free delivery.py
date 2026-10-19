purchase_amount=float(input("enter the purchase amount:-"))

premium_member=True
if purchase_amount>=1000 or premium_member==True:
    print("free delivery")
else:
    print("delivery charge applicable")
