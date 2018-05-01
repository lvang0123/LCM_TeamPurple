num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print()

if(num1 < num2):
  bigger = num2
else:
  bigger = num1
      
while True:
  if((bigger % num2 == 0) and (bigger % num1 ==0)):
    lcm = bigger
    break
  
  bigger += 1
  
print("Least Common Multiple: ", lcm)
