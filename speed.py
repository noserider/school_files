speed = int(input("Enter speed: "))
if speed >= 100:
   print ("You are over 100 mph and face a ban")
elif speed >=90:
    print("Over 90 mph = 6 points and a £250 fine")
elif speed >=80:
    print("Over 80 mph = 3 points and a £125 Fine")
elif speed >=70:
    print("Over 70 mph = £100 fine")
elif speed <= 30:
    print ("You are driving too slow on this road")
else:
   print ("No action")
