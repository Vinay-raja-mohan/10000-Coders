"Print from 1 to 20 numbers"
j=1
while j<=20:
  print(j,end=" ")
  j+=1

print()
print("-------------------")

"Print even numbers between 1-50"
k=1
while k<51:
  if(k%2==0):
    print(k,end=" ")
  k+=1

print()
print("-------------------")

"Print odd nummber from 100-50 in reverse order"
l=100
while l>=50:
  if(l%2!=0):
    print(l,end=" ")
  l-=1

print()
print("-------------------")

"Print squares from number 1 to 10"
a = 1
while a<=10:
  print(a**2,end=" ")
  a+=1

print()
print("-------------------")

"Find the sum of first n natural numbers using while loop"
b = 10
i=1
sum=0
while i<=b:
  sum+=i
  i+=1
print(sum)

print()
print("-------------------")

"Reverse a give number using while loop"
a= 1234
sum=0
while a>0:
  dig = a % 10
  sum = sum *10 + dig
  a//=10
print(sum)

print()
print("-------------------")

"count the number of digits in a given number"
b=1234
sum=0
while b > 0:
  dig = b %10
  b //=10
  sum+=1
print(sum) 

print()
print("-------------------")

"sum of n numbers"
b=1234
sum=0
while b > 0:
  dig = b %10
  b //=10
  sum+= dig
print(sum) 

print()
print("-------------------")

"Multiplication table"
t = 5
a=1

while a <=10:
  print(f"{t} x {a} = {t*a}")
  a+=1

print()
print("-------------------")

"find the factorial of a number "
a=5
sum=1
while a > 0:
  sum *= a
  a-=1
print(sum)

print()
print("-------------------")

