def add(num1,num2):
    answer = num1 + num2
    return answer

first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))

print("Choose an option: (1) Add, (2) Subtract, (3) Divide, (4) Multiply")
choice= int(input())

if choice == 1:
    answer = add(first,second)


print("The answer is",answer)
