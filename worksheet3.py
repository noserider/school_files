#Part1 Hours per week
hourspernight = input("How many hours per night do you sleep? ")
hoursperweek = int(hourspernight) * 7
print ("You sleep",hoursperweek,"hours per week")

#Part2 Hours per month
hourspermonth = float(hoursperweek) * 4.35
print ("You sleep",hourspermonth,"hours per month")

#Part 3 days per month
dayspermonth = float(hourspermonth) / 24
print ("This equates to",dayspermonth,"days per month")
