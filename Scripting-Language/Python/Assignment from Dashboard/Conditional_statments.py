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
  print(f"5% Tax {sal-sal*0.05}")
elif(sal>500000 and sal<1000000):
  print(f"20% Tax {sal-sal*0.2}")
else:
  print(f"30% Tax {sal-sal*0.3}")

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
x = int(input())
y = int(input())
z = int(input())

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




