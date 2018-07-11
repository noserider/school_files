#speed program
speed = int(input("Enter speed: "))
#if is always the first statement
if speed >= 100:
   print ("You are driving dangerously and will be banned")
elif speed >= 90:
   print ("way too fast: £250 fine + 6 Points")
elif speed >= 80:
   print ("too fast: £125 + 3 Points")
elif speed >= 70:
   print ("Please adhere to the speed limits")
elif speed >= 60:
   print ("Perfect")
elif speed <= 30:
   print ("You are driving too slow")   
#else is always the last statement
else:
   print ("No action needed")
