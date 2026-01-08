"Conditional Statements in Python"
n = 10
#if condition:
if n > 0:  #
    print("Positive number")
    print("----------------")

#else condition:
if n>0:
    print("Positive number")
else:
    print("Non-positive number")
  
print("----------------")

#elif condition:
if n > 0:
    print("Positive number")
elif n == 0:
    print("Zero")
else:
    print("Negative number")

print("----------------")



"if a person is eligible to vote or not"
age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
print("----------------")


"a char is vowel or consonant"
char = 'a'
if char in 'aeiouAEIOU':
    print(char, "is a vowel")
else:
    print(char, "is a consonant")


"Check if a number is multiple of 3 and 5"
num = 15

if num%3==0 and num%5==0:
    print(num, "is a multiple of both 3 and 5")
else:
    print(num, "is not a multiple of both 3 and 5")