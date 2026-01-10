"Notes"
n=5200
if n>0:
  d1 = n//500
  print("Number of 500 Rs notes:", d1)
  n = n%500

if n>0:
  d2 = n//200
  print("Number of 200 Rs notes:", d2)
  n = n%200

if n>0:
  d3 = n//100
  print("Number of 100 Rs notes:", d3)
  n = n%100

  "Calculator"
num1 = 10
num2 = 5
operation = '+'
if operation == '+':
    print("Addition:", num1 + num2)

elif operation == '-':
    print("Subtraction:", num1 - num2)

elif operation == '*':      
    print("Multiplication:", num1 * num2) 

elif operation == '/':
    if num2 != 0:
      print("Division:", num1 / num2)
