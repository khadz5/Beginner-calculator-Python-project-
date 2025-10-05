print("Welcome to the simple calculator program in Python !!")# simple welcome message
name = input("What is your name ?") 
print("Hello " + name + " please follow the instructions below") # more personalised experience 
while True: # while loop so continues executing based on conditional input

 num1 = int(input("Please enter your first number: " ))
 num2 = int(input("Please enter your second number: "))
 print("Thank you ,now please choose between the options below") # gives users a choice 
 userAnswer= int(input("Add : 1, Subtract : 2, Multiply : 3, Divide : 4, Quit : 0 = ")) 
 if userAnswer == 1 : # if statements use elif 
    print("You have decided to add your numbers so your result is :" , num1 + num2)
 elif userAnswer == 2:
    print(" You have decided to subtract your numbers so your result is : " , num1 - num2)
 elif userAnswer == 3:
    print(" You have decided to multiply your 2 numbers together so your result is : " , num1 * num2)
 elif userAnswer == 4:
    print(" You have decided to divide your 2 numbers so your result is : " , num1/num2)
 elif userAnswer == 0:
    print(" Goodbye " + name + " ,Thank you for using the calculator program !")
    break
 else:
    print("Invalid input please enter either 1, 2, 3, 4, or 0")


 

