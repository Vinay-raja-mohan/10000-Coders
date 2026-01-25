"Print numbers from 1 to 100 using a for loop."
for i in range(1,101):
  print(i,end=" ")

"Print numbers from 100 to 1 using a for loop."
for i in range(100,0,-1):
  print(i,end=" ")

"Print even numbers between 1 and 50."
for i in range(1,50):
  if i%2==0:
    print(i,end = " ")

"Print odd numbers between 1 and 50."
for i in range(1,50):
  if i%2!=0:
    print(i,end = " ")

"Print multiples of 5 between 1 and 100."
for i in range(1,100):
  if i%5==0:
    print(i,end = " ")

"Find the sum of numbers from 1 to n."
n = int(input())
total = 0
for i in range(1,n+1):
  total += i
print(total)

"Find the sum of even numbers from 1 to n."
n = int(input())
total = 0
for i in range(1,n+1):
  if i%2==0:
    total += i
print(total)

"Find the sum of odd numbers from 1 to n."
n = int(input())
total = 0
for i in range(1,n+1):
  if i%2!=0:
    total += i
print(total)

"Find the product of numbers from 1 to n."
n = int(input())
total = 1
for i in range(1,n+1):
  total *= i
print(total)

"Count the number of digits in a given number."
n = int(input())
count = 0
for i in range(len(str(n))):
  count+=1
print(count)


"Reverse a given number using a for loop."

num = 1234
total = 0
for i in range(len(str(num))):
  last_dig = num%10
  total = total*10 + last_dig
  num//=10
print(total)

"Check whether a number is a palindrome."

num = 121
temp = num
total = 0
for i in range(len(str(num))):
  last_dig = num%10
  total = total*10 + last_dig
  num//=10
if temp == total:
  print("is a palindrome")

"Find the sum of digits of a number."
num = 1234
temp = 0
for i in range(len(str(num))):
  last_dig = num%10
  num//=10
  temp+=last_dig
print(temp)

"Find the product of digits of a number."
num = 1234
temp = 1
for i in range(len(str(num))):
  last_dig = num%10
  num//=10
  temp*=last_dig
print(temp)

"Count how many even and odd digits are in a number."
num = 123
e_sum=0
o_sum=0
for i in range(len(str(num))):
  last_dig = num % 10
  num//=10
  if last_dig % 2 == 0:
    e_sum+=1
  else:
    o_sum+=1
print(o_sum,e_sum)

"Find the factorial of a given number."
dig = 5
temp=1
for i in range(1,dig+1):
  temp*=i
print(temp)

"Check whether a number is prime."
num = 7
temp = 0
for i in range(1,num+1):
  if(num%i==0):
    temp+=1
if(temp==2):
  print("Prime")
else:
  print("Not Prime")

"Check whether a number is an Armstrong number."
num = 153
temp = num
len = len(str(num))
total = 0
for i in range(len):
  last_dig=num%10
  total += last_dig**len
  num//=10
if(temp==total):
  print("Armstrong")
else:
  print("Not Armstrong")

"Check whether a number is a perfect number."
num = int(input())
total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if total == num:
    print("Perfect")
else:
    print("Not Perfect")