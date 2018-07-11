name = ''
 
print('What is my name?')
name = input()
while name != 'Simon':
     print("Guess Again")
     print('What is my name?')
     name = input()
while name == 'Simon':
   if name == 'Simon':
      print("Got it!")
   break
