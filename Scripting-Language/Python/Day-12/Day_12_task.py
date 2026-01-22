"Print sum of even,odd , prime digits in a number"

num1 = 23456
sumE=0
while num1>0:
  dig = num1%10
  num1 //=10
  if(dig%2==0):
    sumE+=dig
print("sum of even numbers",sumE)

num2 = 23456
sumO=0
while num2>0:
  digi = num2 % 10
  num2 //= 10
  if(digi%2!=0):
    sumO+=digi
print("Sum of odd numbers", sumO)

num3 = 23456
sumP = 0
while num3>0:
  digit = num3 % 10
  num3 //= 10

  add = 0
  for i in range (1,digit+1):
    if digit%i==0:
      add+=1
  if add==2:
    sumP+=digit

print(sumP)


