numberofppl=int(input("number of ppl: "))
traveldistanceinkm =float(input("travel distance in km : "))
vehiclemileage=float(input("vehicle mileage(km/litre:- "))
petrolpriceperlitre=float(input("petrol price per litre;- "))
fuelused=traveldistanceinkm/vehiclemileage
totalfuelprice=fuelused*petrolpriceperlitre
costperperson=totalfuelprice/numberofppl
print(fuelused)
print(totalfuelprice)
print(costperperson)


