import time as datetime

def printTitle():
    print("========================================")
    print("Welcome to the TV Listings Program")
    print("Today's date:",datetime.strftime("%x"))
    print("Current time:",datetime.strftime("%X"))
    print("========================================")

def printProgram(program,time):
    print()
    print(program,"is on tomorrow at",time)
    print("Press 'Enter' to get the next program")
    input()
    print()

programs = ["Coronation Street","Eastenders","Emmerdale","Hollyoaks"]
times = ["20:00","19:30","19:00","18:30"]

for counter in range(4):
    printTitle()
    program = programs[counter]
    time = times[counter]
    printProgram(program,time)

printTitle()
input("Press enter to close this program")
