noofseconds=float(input("enter the seconds:- "))

hours=noofseconds//3600
remaining=noofseconds%3600
minutes=remaining//60
seconds=remaining%60

print(hours)
print(minutes)
print(seconds)