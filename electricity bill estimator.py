unitconsumed=float(input("enter unit consumed:-"))
costperunit=float(input("enter cost per unit:-"))
totaleletricitycharge=unitconsumed*costperunit
fivepercentageoftotalelectricitycharge=0.05*totaleletricitycharge
finalamount=totaleletricitycharge+fivepercentageoftotalelectricitycharge

print(totaleletricitycharge)
print(finalamount)
