import time as datetime

def displayTime():
    print("========================================")
    print("Welcome to the TV Listings Program")
    print("Today's date:",datetime.strftime("%x"))
    print("Current time:",datetime.strftime("%X"))
    print("========================================")

def displayNext():
    print()
    print(program,"is on tomorrow at",time)
    print("Press 'Enter' to get the next program")
    input()
    print()

programs = ["Coronation Street","Eastenders","Emmerdale","Hollyoaks"]
times = ["20:00","19:30","19:00","18:30"]

displayTime()

program = programs[0]
time = times[0]

displayNext()

# Next show

displayTime()

program = programs[1]
time = times[1]

displayNext()

# Next show

displayTime()

program = programs[2]
time = times[2]

displayNext()

# Next show

displayTime()

program = programs[3]
time = times[3]

displayNext()

# Finish

displayTime()

input("Press enter to close this program")
