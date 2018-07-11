#program start sleep calculator

#this is a comment and doesnt affect my program
#hourspernight is a variable
#input and print are functions

#how many hours do you sleep per week
hourspernight = input("How many hours per night do you sleep? ")
hoursperweek = int(hourspernight) * 7
print ("You sleep",hoursperweek,"hours per week")

#float is used as we are multiplying by a decimal
#round is used so that we limit to two decimal places
hourspermonth = float(hoursperweek) * 4.35
hourspermonth = round(hourspermonth,2)
print ("You sleep",hourspermonth,"hours per month")

#calculate hours per year
hoursperyear = int(hourspermonth) * 12
print ("You sleep",hoursperyear, "hours per year")

