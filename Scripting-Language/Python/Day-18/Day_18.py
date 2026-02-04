# # Print the characters in the prime index
# str1 = "abcdefghijklmnopqrstuvwxyz"

# for i in range(1,len(str1)):
#   if i>1:
#     for j in range(2,i):
#       if i%j==0:
#         break
#     else:
#       print(str1[i],i)
# 
# #replace vowels with *

# str2 = "zqwaexsrcdtvfygbuhnijmolp"
# temp2 = ''
# for i in str2:
#   if i in "aeiou":
#      temp2+= "*"
#   else:
#      temp2+=i
# print(temp2)
# print("----------")

# str3 = "zqwaexsrcdtvfygbuhnijmolp"
# temp3 = ''
# for i in str3:
#    if i in 'aeiou':
#       str3=str3.replace(i,"*")
# print(str3)
# 
# # check if 2 strings are anagrams
# a = 'tea'
# b = 'eat'
# 
# if sorted(a) == sorted(b):
#   print("anagram")
# 
# from collections import Counter
# print(Counter(a))
# 
# temp9= {}
# temp10={}
# for i in a:
#   if i in temp9:
#     temp9[i] +=1
#   else:
#     temp9[i] = 1

# for i in b:
#   if i in temp10:
#     temp10[i] +=1
#   else:
#     temp10[i] = 1

# if temp9 == temp10:
#   print("anagram")
# else:
#   print("Not anagram")
# 
# reverse each word in a string
k = "reverse each word string".split()

for i in range(len(k)):
  temp3 = ''
  for j in k[i]:
    temp3 = j + temp3
  k[i] = temp3
print(" ".join(k))

  