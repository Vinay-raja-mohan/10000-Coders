# 'Sum of all values in Dictionary'

# res ={'a':10,'b':20,'c':30}
# sum=0
# for i in res.values():
#   sum+=i

# print(sum)

# 'print the first n prime numbers'
# n = 5
# temp = []
# for i in range(1,100):
#   count = 0
#   for j in range(1,i):
#     if i%j==0:
#       count +=1
#   if  count == 1:
#     temp.append(i)
# print(temp)
# for i in range(0,n):
#   print(temp[i])


# l=[]
# for x in range(2,50):
#   for y in range(2,x):
#     if x%y==0:
#       break
#   else:
#     l.append(x)
  
#   if len(l)==n:
#     print(l)
#     break


# cou = 0
# p=2
# while n>cou:
#   is_prime=True
#   for x in range(2,p):
#     if p%x==0:
#       is_prime = False
#       break

#   if is_prime:
#     print(p)
#     cou+=1
#   p+=1

# "store reversed of the keys as their values"

# word= ['cat','dog','bat']

# tem = {}

# for i in word:
#   r =''
#   for j in i:
#     r = j + r
#   tem[i]=r
# print(tem)

# "print their ascii values as keys and values {'a':65,'b':66}"
# temp={}
# for i in range(65,91):
#   temp[chr(i)]=i
# print(temp)

# "if input is vowel the print it with its ord , if not then just print the character"
# temp = {}
# a = input("Enter a char: ")
# if a in 'aeiouAEIOU':
#   b = a.swapcase()
#   temp[b] = ord(b)
#   print(temp)

# else:
#   print(a)


# "merge 2 dicts"
# a = {'a':1,'b':2,'c':3}
# b = {'d':4,'e':5}

# for i,j in b.items():
#   a[i] = j
# print(a)

# res = {**a,**b}
# print(res)


res = [10,11,12,13,14,15,16,17]
temp_e = []
temp_o = []
temp={}
for i in res:
  if i%2==0:
    temp_e.append(i)
  else:
    temp_o.append(i)

temp['even']=temp_e
temp['odd'] = temp_o
print(temp)

d={}

d['even']=[x for x in res if x%2==0]
d['odd'] = [y for y in res if y%2!=0]
print(d)

  