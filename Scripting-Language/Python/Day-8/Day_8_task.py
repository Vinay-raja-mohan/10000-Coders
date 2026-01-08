"1. Check whether a number is positive or negative"
a=10
if a>=0:
    print("Positive Number")
else:
    print("Negative Number")

"2. Check whether a number is even or odd."
b=7
if b%2==0:
    print("Even Number")
else:
    print("Odd Number")

"3. Check whether a number is divisible by 5."
c=20
if c%5==0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")

"4. Find the greater of two numbers."
d=15
e=25
if d>e:
    print("Greater number is", d)
else:
    print("Greater number is", e)

"5. Find the greatest of three numbers."
f=12
g=9
h=20

if f>g and f>h:
    print("Greatest number is", f)
elif g>f and g>h:
    print("Greatest number is", g)
else:
    print("Greatest number is", h)

"6. Check whether a year is a leap year."
year=2020
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap Year")
else:
    print("Not a Leap Year")

"7. Check whether a person is eligible to vote."
age=18
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

"8. Check whether a character is a vowel or consonant."
char='a'
if char in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")

"9. Check whether a number is divisible by both 3 and 7."
i=21
if i%3==0 and i%7==0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both 3 and 7")

"10. Check whether a number is single-digit, double-digit, or more."
j=123
if j<10:
    print("Single digit")
elif j<100:
    print("Double digit")
else:
    print("More than double digit")