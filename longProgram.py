import time as datetime
programs = ["Coronation Street","Eastenders","Emmerdale","Hollyoaks"]
times = ["20:00","19:30","19:00","18:30"]
def displayTime():
    print("========================================")
    print("Welcome to the TV Listings Program")
    print("Today's date:",datetime.strftime("%x"))
    print("Current time:",datetime.strftime("%X"))
    print("========================================")
displayTime()

program = programs[0]
time = times[0]

print()
print(program,"is on tomorrow at",time)
print("Press 'Enter' to get the next program")
input()
print()

# Next show

displayTime()

program = programs[1]


print()
print(program,"is on tomorrow at",time)
print("Press 'Enter' to get the next program")
input()
print()

print()
print(program,"is on tomorrow at",time)
print("Press 'Enter' to get the next program")
input()
print()

# Finish

displayTime()

input("Press enter to close this program")
