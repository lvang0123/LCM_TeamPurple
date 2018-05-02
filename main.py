num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

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
#if BIGGER is divisible by both input numbers without a remainder, assign LCM as the value of BIGGER
    lcm = bigger
#break out of loop
    break
  #else add 1 to bigger, and continue the loop
  bigger += 1
  
#when broken out of, print the value of LCM
print("Least Common Multiple: ", lcm)
