#int = interger
#we have two variable defined hourspernight & hoursperweek
hourspernight = input("How many hours per night do you sleep? ")
hoursperweek = int(hourspernight) * 7
print ("You sleep",hoursperweek,"hours per week")

#round gives a whole number answer or a specific number of decimal points
hourspermonth = float(hoursperweek) * 4.35
hourspermonth = round(hourspermonth,2)
print ("You sleep",hourspermonth,"hours per month")

hoursperyear = float(hourspermonth) * 12
hoursperyear = round(hoursperyear,2)
print ("You sleep",hoursperyear,"hours per year")
