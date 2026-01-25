"Question 1"
hindi = int(input())
english = int(input())
telugu = int(input())
math = int(input())
science = int(input())

if hindi < 40 or english < 40 or telugu < 40 or math < 40 or science < 40:
  print("Fail")

else:
  sum=hindi+english+telugu+math+science
  per = (sum/5)
  print(f"{per}% Pass")


"Question 2"
year = int(input())
if(year%4==0 and year%100!=0)  or (year%400==0):
  print("Leap Year")

else:
  print("Not Leap Year")


"Question 3"
sal = int(input())
if(sal <= 250000):
  print("No Tax")
elif(sal>250000 and sal<=500000):
  print(f"5% Tax {sal*0.05}")
elif(sal>500000 and sal<1000000):
  print(f"20% Tax {sal*0.2}")
else:
  print(f"30% Tax {sal*0.3}")

"Question 4"
import math
a = int(input())
b= int(input())
c = int(input())

if(a+b>c and b+c>a and c+a>b):
  s=(a+b+c)/2
  area = math.sqrt(s*(s-a)*(s-b)*(s-c))
  print("area =",area)

"Question 5"
a = int(input())
b = int(input())
c = int(input())

if a>b and a>c:
  print("Largest",a)
elif b>a and b>c:
  print("Largest",b)
else:
  print("Largest",c)

if a<b and a<c:
  print("Smallest",a)
elif b<a and b<c:
  print("Smallest",b)
else:
  print("Smallest",c)

if(a==b and b==c):
  print("Equal")
  
"Question 6"
ch = input()

if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

"Question 7"
password = input()
special_characters = "!@#$%^&*(),.?\":{}|<>"
digit,special = 0,0

for i in password:
  if  i.isdigit():
    digit+=1
  if i in special_characters:
    special+=1
if digit>=1 and special >= 1 and len(password)>=8:
  print('Valid Password')

"Question 8"

distance = int(input())
age = int(input())

if(distance<=10):
  fair = 10

elif distance > 10 and distance < 30:
  fair = 20

else:
  fair = 30

if age > 50:
  fair = fair - fair*0.2

print(fair)

"Question 9"

attendace = int(input("in %"))
certi = input()
if attendace >=75 and certi == "yes":
  print("Eligible")

"Question 10"

amount = int(input())
a_type = input()
if a_type == "Savings":
  intrest = amount*0.04
elif a_type == "Current":
  intrest =  amount*0.02
elif a_type == "Fixed":
  intrest = amount*0.06

print (intrest)

"Question 11"

num = int(input())
addi = 0
for i in range(1,num+1):
  if num%i == 0:
    addi += 1
  
if(addi==2):
  print("Prime number")
elif addi > 2:
  print("Composite")
elif addi == 1:
  print("netiher")


"Question 12"

temp = int(input())
if temp < 10:
  print("Very Cold")
elif temp >=10 and temp <=20:
  print("Cold")
elif temp>=21 and temp <=30:
  print("Warm")
else:
  print("Hot")

"Question 13"

amt = int(input())
cou = input()

if amt >= 1000:
    dis = amt * 0.20
elif amt >= 500:
    dis = amt * 0.10
else:
    dis = 0

if cou == "yes":
    dis = dis + 50   

print(amt - dis)



"Question 14"

signal = input()

if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Ready")
elif signal == "Green":
    print("Go")
else:
    print("Invalid Signal")


"Question 15"

time = int(input())

if time >= 5 and time < 12:
    print("Morning")
elif time >= 12 and time < 17:
    print("Afternoon")
elif time >= 17 and time < 21:
    print("Evening")
else:
    print("Night")


"Question 16"

age = int(input())
health = input()
smoking = input()

if age >= 18 and age <= 60 and health == "good" and smoking == "no":
    print("Eligible")
else:
    print("Not Eligible")


"Question 17"

amount = int(input())

if amount == 199:
    print("1.5GB/day")
elif amount == 299:
    print("2GB/day")
elif amount == 499:
    print("Unlimited")
else:
    print("Invalid Plan")


"Question 18"

stc = input()
bal = input()
deli = input()

if stc == "yes" and bal == "yes" and deli == "yes":
    print("Order Placed")
else:
    print("Order Not Placed")


"Question 19"

rating = int(input())
experience = int(input())

if rating >= 4 and experience >= 5:
    print("Promotion Eligible")
else:
    print("Not Eligible")


"Question 20"

marks = int(input())
attendance = int(input())

if attendance > 90:
    marks = marks + 5

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

