# Print the characters in the prime index
str1 = "abcdefghijklmnopqrstuvwxyz"

for i in range(1,len(str1)):
  if i>1:
    for j in range(2,i):
      if i%j==0:
        break
    else:
      print(str1[i],i)

#replace vowels with *

str2 = "zqwaexsrcdtvfygbuhnijmolp"
temp2 = ''
for i in str2:
  if i in "aeiou":
     temp2+= "*"
  else:
     temp2+=i
print(temp2)
print("----------")

str3 = "zqwaexsrcdtvfygbuhnijmolp"
temp3 = ''
for i in str3:
   if i in 'aeiou':
      str3=str3.replace(i,"*")
print(str3)

# check if 2 strings are anagrams
a = 'tea'
b = 'eat'

if sorted(a) == sorted(b):
  print("anagram")

from collections import Counter
print(Counter(a))

temp9= {}
temp10={}
for i in a:
  if i in temp9:
    temp9[i] +=1
  else:
    temp9[i] = 1

for i in b:
  if i in temp10:
    temp10[i] +=1
  else:
    temp10[i] = 1

if temp9 == temp10:
  print("anagram")
else:
  print("Not anagram")

# reverse each word in a string
k = "reverse each word string".split()

for i in range(len(k)):
  temp3 = ''
  for j in k[i]:
    temp3 = j + temp3
  k[i] = temp3
print(" ".join(k))

k = "cap starting of each start"
temp1 = ""
for x in range(0,len(k)):
  if x == 0:
    temp1+=k[x].upper()
  elif k[x-1] == " ":
    temp1+= k[x].upper()
  else:
    temp1+=k[x]
print(temp1)

# Remove duplicates from list and sort
k =[10,20,30,40,10,20]
d=list(set(k))
d.sort()
print(d)
temp = []
for x in k:
  if x not in temp:
    temp.append(x)

# Sum of int and float from list
j = [10,11,12,3.2,'python',10.2]
temp = 0 
for i in j:
  if type(i)==int or type(i)==float:
    temp+= i
print(temp)

# Find minimum element in list
k = [10,11,12,5,2]
temp = k[0]
for i in k:
  if temp > i:
    temp = i
print(temp)
  
# Filter even numbers and collect strings
l = [10,20,11,13,'c++','python',3+2j]
temp=[]

for i in l:
  if type(i)==int and i%2==0:
    print(i)
  if type(i)== str:
    temp.append(i)
print(temp)

# Double even numbers in list
j = [10,11,12,13]
temp = []
for i in j:
  if i%2==0:
    temp.append(i*2)
  else:
    temp.append(i)
print(temp)

for i in range(0,len(j)):
  if i%2==0:
    j[i] = j[i]*2
print(j)


    