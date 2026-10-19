datavailable=float(input("data available in gb"))
no_of_days_inmonth=int(input("no.of.days in month"))
gb_mb=datavailable*1024

avrgMBperday=gb_mb/no_of_days_inmonth
remaining=gb_mb-500
remaininginGB=remaining/1024

print(gb_mb)
print(avrgMBperday)
print(remaininginGB)
