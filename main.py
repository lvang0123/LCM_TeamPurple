#Python Team Project - Least Common Multiple 
#This program will prompt the user for two number inputs. The program will then try to find the least common multiple for those two numbers.
#May 1, 2018 - Ben, Dan, Kyle, Lisa, and Lia all worked on this program together during class time.

#Welcoming the user
print("Welcome to the Least Common Multiple program!")
print()

#Declaring variables
rerun = "Y"

#Rerunning the program if the user inputs 'Y' at the end of the program
while rerun.lower().upper() != "N":
  
  #Prompting the user to input two numbers 
  print("Please enter two numbers that you want to find the least common multiple for.")
  print()
  
  while True:
    try:
      num1 = int(input("Number 1: "))
      break
    except ValueError:
      print()
      print("*** ERROR: Not an integer ***")
      print()
      
  while True:
    try:
      num2 = int(input("Number 2: "))
      break
    except ValueError:
      print()
      print("*** ERROR: Not an integer ***")
      print()
  
  print()
  
  #if the second number entered is larger than the first
  if(num1 < num2):
    #the bigger of the two is logically the second one, and therefore BIGGER is assigned this value
    bigger = num2
    #the else statement of this if statement
  else:
    bigger = num1
        
  #while true, loop initialization
  while True:
    if((bigger % num2 == 0) and (bigger % num1 ==0)):
  #if BIGGER is both devisible by both input numbers without a remainder, assign LCM as the value of BIGGER
      lcm = bigger
  #break out of loop
      break
    #else add 1 to bigger, and continue the loop
    bigger += 1
    
  #when broken out of, print the value of LCM
  print("Least Common Multiple: ", lcm)
  print()
  
  #Prompting the user to rerun the program or end it
  while True: 
    print("Would you like to rerun the program?")
    rerun = input("Enter Y to rerun it or N to end it: ")
    
    if rerun.lower().upper() == "Y":
      print()
      print('---------------------------------------')
      print()
      break
    elif rerun.lower().upper() == "N":
      print()
      break
    else:
      print()
      print("*** ERROR: Must enter a Y or N ***")
      print()

#Informing the user that the program has ended
print("Thank you for using the Least Common Multiple program!")
