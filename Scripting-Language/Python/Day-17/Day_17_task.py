# Reverse a string without using slicing or reverse().
str1 = "vinay"
temp = ''
for chr in str1:
  temp = chr + temp
print (temp)
print("-----------------------------")

# Check whether a string is a palindrome.
str2 = "vinaniv"
temp2 = str2[::-1]
if str2 == temp2:
  print("palindrome")
else:
  print("Not Palindrome")
print("-----------------------------")
# Count the frequency of each character in a string.
str3 = "aaaabbbccc"
temp3 = {}
for i in str3:
  if i in temp3:
    temp3[i]+=1
  else:
    temp3[i] = 1
print(temp3)
print("-----------------------------")
# Find the first non-repeating character in a string.
str4 = "aaabbbbdeeef"
temp4 = {}
for chr4 in str4:
  if chr4 in temp4:
    temp4[chr4] +=1
  else:
    temp4[chr4] = 1

for i in str4:
  if temp4[i] == 1:
    print(i)
    break
print("-----------------------------")

# Remove duplicate characters from a string.
str5 = 'aaabbcdddef'
temp5 = ''

for i in str5:
  if i not in temp5:
    temp5 += i
print(temp5)
print("-----------------------------")

# Find the maximum occurring character in a string.
str6 = "aaaaaabbbbbbbbcccdddddeeeeee"
temp6 ={}
for i in str6:
  if i in temp6:
    temp6[i]+=1
  else:
    temp6[i] = 1

s_temp = 0
char = ''
for j in temp6:
  if temp6[j]>s_temp:
    s_temp = temp6[j]
    char = j
print(char,temp6[char])
print("-----------------------------")

# Count the number of vowels and consonants in a string.
str7 = "aajfnebuvbucvqqckjqbvbqonknassnznadqbipokmsmazlioueyhunt"
vowles = 0
conso = 0
for i in str7:
  if i in "aeiouAEIOU":
    vowles+=1
  else:
    conso +=1   
print(vowles,conso) 
print("-----------------------------")

# Reverse each word in a string.
str8 = " always follow dreams"
s_str8 = str8.split()

for idx in range(len(s_str8)):
    temp8 = ''
    for ch in s_str8[idx]:
        temp8 = ch + temp8
    s_str8[idx] = temp8

ss_str8 = " ".join(s_str8)
print(ss_str8)
print("-----------------------------")
# Check whether two strings are anagrams.
str9 = "listen"
str10 = 'silent'

temp9= {}
temp10={}
for i in str9:
  if i in temp9:
    temp9[i] +=1
  else:
    temp9[i] = 1

for i in str10:
  if i in temp10:
    temp10[i] +=1
  else:
    temp10[i] = 1

if temp9 == temp10:
  print("anagram")
else:
  print("Not anagram")
print("-----------------------------")

# Replace spaces with special characters (e.g., @)
str11 = "mknbuvy hbjnbvh gjknobvh g"
r_str11 = str11.replace(" ","@")
print(r_str11)
print("-----------------------------")