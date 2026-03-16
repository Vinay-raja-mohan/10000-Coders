# Write a Python program that takes a number from the user and prints:
# Number
#  Its Square
# Its cube

a=int(input("give a number: "))
print(a,a**2,a**3)

# 2.Write a Python program to check whether a number entered by the user is:
# Positive
# Negative
# Zero
b = int(input("give a number: "))
if b > 0:
  print("Positive")
elif b<0:
  print("negitive")
else:
  print("zero")

# 3. Write a Python program to print the multiplication table of a given number up to 10.
c=int(input("give a number: "))
for i in range(1,11):
  print(f"{c} x {i} = {c*i}")
#    4. Write a Python program that:
# Takes 5 numbers from the user
# Stores them in a list
# Prints:
# Largest number
# Smallest number
# Sum of all numbers
temp=[]
for i in range(5):
  a=int(input())
  temp.append(a)
print(min(temp),' ',max(temp), ' ',sum(temp))


#  5. Write a Python function that checks whether a number is a prime number.
a = int(input("Enter a number: "))

if a <= 1:
    print(a, "is not a prime number")
else:
    for i in range(2, a):
        if a % i == 0:
            print(a, "is not a prime number")
            break
    else:
        print(a, "is a prime number")
