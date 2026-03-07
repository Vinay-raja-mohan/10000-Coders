import random

while True:
    num = random.randint(0,5)
    print(num)
    # a = int(input("Guess a number from 1-5: "))
    count=0
    while True:
      a = random.randint(0,5) 
      print(a,end=' ')
      count+=1
      if num == a:
          print()
          print("you guessed it ".upper())
          break
    break
print(f"Guessed it in {count}",end=' ')
if count == 1:
   print('attempt')
else:
   print('attempts')