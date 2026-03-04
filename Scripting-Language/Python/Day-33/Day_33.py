# 'modules' - VARIABLES+FUNCTIONS+CLASSES
# 1. predefined modules
# 2. User defined modules
# 3. Third party modules

# 1. PREDEFINED MODULES
    #  Ex:-random,path,datetime,time

# 2. USERDEFINED MODULES
    #  Ex:- .py files

# 3. THIRDPARTY MODULES
    #  Ex:- pandas,numpy  -> pip install pandas


# from file_1 import variable_name,function     calling any function or variable from file

# import file_1     calling the whole file

import random

# phone number print
for x in range(5):
    print(f"+91 {random.randint(6000000000,9999999999)}")

# guess a number
while True:
    num = random.randint(0,5)
    a = int(input("Guess a number : "))
    if num == a:
        print("you guessed it ".upper())
        break
  
# dice and score
score1 =0
score2 =0
while True:
    input("Player1 Press Enter")
    a=random.randint(1,6)
    score1+=a
    print("P1 =",score1)
    input("Player2 Press Enter")
    b = random.randint(1,6)
    score2+=b
    print("P2 =",score2)
    if score1>=20 or score2>=20:
        break
    
if score1>score2 :
    print("Player 1 WON")
elif score1<score2 :
    print("Player 2 WON")
else:
    print("DRAW")

# generate password
a = int(input("How many numbers you want : "))
emp =''
for x in range(a):
    p=random.choice("!@#$%^&*()_+=?>/<,.;:'}[]{")
    emp+=p
b = int(input("Enter number of strings : "))
for x in range(b):
    q=random.choice("abcdefghijklmnopqrstuvwqyx")
    emp+=q
c = int(input("Enter the number of numbers"))
for x in range(c):
    r=random.choice("1234567890")
    emp+=r
print(emp)
