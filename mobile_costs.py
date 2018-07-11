# program start

# input name
name = input("What is your name? ")
network = input("Please enter which network you use? ")

# input number of minutes and texts used this month
minutes = input("How many minutes have you used this month? ")
texts = input("How many texts have you used this month? ")

# arithmetic and rounding
minutes = round(float(minutes) * 0.10,2)
texts = round(float(texts) * 0.05,2)

# declare new variables and VAT constant
total_bill = minutes+texts
VAT_rate = 0.2
VAT_cost = round(total_bill * VAT_rate,2)











# Add blank line so make layout look better
print ("\n")

# output
print (name, "your bill is as follows:")
print ("\nYour monthly minute costs with",network,"is £",minutes)
print ("Your monthly texts costs with",network,"is £",texts)

print ("\nYour total monthly bill is £",total_bill)
print ("VAT = £",VAT_cost)
print("____________________________________________________")
print ("\nYour total monthly bill including VAT is £",round(total_bill + VAT_cost,2))


#Holds the screen until ENTER pressed to read results if using windows console
input("\nPress ENTER to exit the program")
