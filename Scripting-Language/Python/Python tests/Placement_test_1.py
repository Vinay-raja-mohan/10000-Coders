# # Numbers & Operators 
# 1. Write a program to add two numbers. 
a=3
b=2
print(a+b)
# 2. Find the difference between two numbers. 
print(a-b)
# 3. Multiply two numbers entered by the user. 
a=int(input("enter a number"))
b=int(input("enter a number"))
print(a*b)
# 4. Divide two numbers and print the quotient. 
print(a//b)
# 5. Find the remainder when a number is divided by another. 
print(a%b)
# 6. Check whether a number is even or odd. 
if a%2==0:
  print("even")
else:
  print("odd")
# 7. Find the square of a number. 
print(a**2)
# 8. Find the cube of a number. 
print(a**3)
# 9. Calculate simple interest. 
si=((p*t*r)/100)


# Conditional Statements 
# 11. Check whether a number is positive, negative, or zero. 
if a>0:
  print("positive")
elif a<0:
  print("negitive")
else:
  print("zero")
# 12. Check whether a number is divisible by 5. 
if a%5==0:
  print("divisible by 5")
else:
  print("not divisible by 5")
# 13. Find the greatest of two numbers. 
if a>b:
  print(a,"is the greatest")
else:
  print(b,"is the greatest")
# 14. Find the smallest of two numbers. 
if a<b:
  print(a,"is the smallest")
else:
  print(b,"is the smallest")
# 15. Check whether a year is a leap year. 
if year%100 !=0 and year % 4 == 0 or year % 400 ==0:
  print("it is a leap year")
else:
  print("it is not a leap year") 
# 16. Check whether a number is a multiple of both 3 and 5. 
if a%3==0 and a%5==0:
  print("divisble by both")
else:
  print("not disivible by both")
# 17. Print “Pass” if marks ≥ 40 else “Fail”. 
if marks >= 40:
  print("pass")
else:
  print("fail")
# 18. Check whether a number is a two-digit number. 
if 10 <= abs(a) <= 99:
  print("a two digit number")
else:
  print("not a 2 digit number")
# 19. Check whether a character is a vowel or consonant. 
if a.lower() in "aeiou":
  print("it is a vowel")
else:
  print("consonant")
# 20. Check whether a number is greater than 100. 
if a>100:
  print("greater")
else:
  print("not greater than 100")


# Loops (Basic) 
# 21. Print numbers from 1 to 10. 
for i in range(1,11):
  print(i)
# 22. Print numbers from 10 to 1. 
for i in range(10,0,-1):
  print(i)
# 23. Print even numbers from 1 to 20. 
for i in range(0,21):
  if i%2==0:
    print(i)
# 24. Print odd numbers from 1 to 20. 
for i in range(0,21):
  if i%2!=0:
    print(i)
# 25. Print the multiplication table of a number. 
a=5
for i in range(1,11):
  print(f"{a} x {i} = {a*i}")
# 26. Find the sum of numbers from 1 to N. 
n = 10
sum =0
for i in range(1,n+1):
  sum+=i
print(sum)
# 27. Find the factorial of a number. 
mul =1
for i in range(1,n+1):
  mul *= i
print(mul)  
# 28. Count digits in a number. 
print(len(str(n)))
# 29. Reverse a number. 
print(int(str(n)[::-1]))
# 30. Check whether a number is a palindrome. 
sum = 0
temp = n
while n >0:
  ld = n %10
  n//=10
  sum = sum*10 + ld
if temp == sum:
  print("it is a palindrome")


# MEDIUM LEVEL (31–60) 
# Strings 
# 31. Print each character of a string. 
for i in range(0,len(n)):
  print(n[i])
# or
for i in n:
  print(i,end=" ")
# 32. Count the number of characters in a string. 
print(len(n))
# 33. Count vowels in a string. 
count =0
for i in n:
  if i.lower() in "aeiou":
    count += 1
print(count)
# 34. Count consonants in a string. 
count =0
for i in n:
  if i.lower() not in "aeiou":
    count += 1
print(count)
# 35. Reverse a string. 
print(n[::-1])
# 36. Check whether a string is a palindrome.
emp=""
for i in n:
  emp = i + emp
if emp == n:
    print("Palindrome")
else:
    print("Not palindrome")
# 37. Convert a string to uppercase. 
print(n.upper())
# 38. Convert a string to lowercase. 
print(n.lower())
# 39. Count spaces in a string. 
count = 0
for i in n:
  if i == " ":
    count+=1
# 40. Count digits in a string. 
count = 0
for i in n:
  if i.isdigit():
    count +=1


# Lists 
# 41. Create a list and print all elements.
l = ["a","e","i","o","u"]
for i in l:
  print(i)
# 42. Find the length of a list. 
print(len(l))
# 43. Find the sum of list elements.
print(sum(l))
# 44. Find the maximum element in a list. 
print(max(l))
# 45. Find the minimum element in a list. 
print(min(l))
# 46. Count even numbers in a list. 
count = 0
for i in n:
  if i % 2 ==0 :
    count +=1
# 47. Count odd numbers in a list. 
count = 0
for i in n:
  if i % 2 !=0:
    count +=1
# 48. Print only positive numbers from a list. 
for i in n:
  if i > 0:
    print(i)
# 49. Print only negative numbers from a list. 
for i in n:
  if i < 0:
    print(i)
# 50. Reverse a list. 
l.reverse()
print(l)


# Tuples 
# 51. Create a tuple and print all elements. 
l = (1,2,3,4,5)
for i in l:
  print(i)
# 52. Find the length of a tuple. 
print(len(l))
# 53. Find the maximum element in a tuple. 
print(max(l))
# 54. Find the minimum element in a tuple. 
print(min(l))
# 55. Convert a tuple into a list. 
a = list(l)
# 56. Check whether an element exists in a tuple. 
e=1
for i in l:
  if i == e:
    print("element exists")
# 57. Count occurrences of an element in a tuple. 
print(l.count(2))
# 58. Print tuple elements using a loop. 
for i in l:
  print(i)
# 59. Create a tuple with mixed data types.
l=(1,1.2,"a",[1,2],{"a":1}) 
# 60. Print index and value of each tuple element. 
for i in range(0,len(l)):
  print(i,"=",l[i])


# DICTIONARY LEVEL (61–80) 
# 61. Create a dictionary and print it. 
d={"a":1,"b":2}
print(d)
# 62. Print all keys of a dictionary. 
for i in d.keys():
  print(i)
# 63. Print all values of a dictionary. 
for i in d.values():
  print(i)
# 64. Print key-value pairs of a dictionary. 
for k,v in d.items():
  print(k,"=",v)
# 65. Count the number of keys in a dictionary. 
count = 0
for i in d.keys():
  count +=1
# 66. Check whether a key exists in a dictionary. 
k = 'a'
for i in d.keys():
  if i == k:
    print("it exists")
# 67. Add a new key-value pair to a dictionary. 
d.update({"c":3})
# or
d["c"]  = 3
# 68. Update the value of an existing key. 
d.update({"c":3})
# 69. Delete a key from a dictionary. 
d.pop(k)
# 70. Create a dictionary from user input. 
for i in range(3):
  k = input("key ")
  v = input("value ")
  d[k] = v


# Dictionary Logic Problems 
# 71. Count frequency of each character in a string using dictionary. 
a = "aaabbcsdseeaa"
temp ={}
for i in range(0,len(a)):
  if a[i] not in temp:
    temp[a[i]] =1
  else:
    temp[a[i]] +=1
# 72. Count frequency of elements in a list using dictionary. 
l=[1,2,3,3,4,1,4,2]
temp = {}
for i in l:
  if l not in temp:
    temp[i] = 1
  else:
    temp[i]+=1
# 73. Find the key with maximum value in a dictionary. 
max_k= None
max_v = float('-inf')

for k,v in d.items():
  if v > max_v:
    max_v = v
    max_k = k
print(max_k)
# 74. Find the key with minimum value in a dictionary. 
max_k= None
max_v = float('inf')

for k,v in d.items():
  if v < max_v:
    max_v = v
    max_k = k
print(max_k)
# 75. Merge two dictionaries. 
for k,v in d2.items():
  d1[k]=v
# 76. Create a dictionary with numbers (1–5) and their squares. 
temp = {}
for i in range(1,6):
  temp[i] = i**2
print(temp)
# 77. Create a dictionary from two lists (keys and values). 
key=['name','age','city']
value=['john',25,'new york']
temp ={}
for i in range(len(key)):
    temp[key[i]] = value[i]
print(temp)
# 78. Sum all values in a dictionary. 
sum = 0
for v in d.values():
  sum += v
print(sum)
# 79. Print only keys whose value is greater than 50. 
for k,v in d.items():
  if v > 50:
    print(k)
# 80. Convert dictionary keys into a list. 
temp = []
for k in d.keys():
  temp.append(k)
print(temp)