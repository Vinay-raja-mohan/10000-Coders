# Dictionary iteration using items()
s = {'a':10,'b':20}

for x in s.items():
  print(x)

# Create dictionary from list of tuples
h = dict([('a',10),('b',20)])
print(h)

# Reverse dictionary (swap keys and values)
j = {'name':'ajay','mobile':123456789}
temp = {}
for k,v in j.items():
  temp[v] = k

print(temp)

# Create dictionary with word lengths
words = ['apple','banana','kiwi']
temp ={}
tem = {}
for k in words:
  temp[k] = len(k)

for i,j in temp.items():
  tem[j] = i

print(temp)
print(tem)

# Count characters in each word
for k in words:
  count = 0
  for j in k:
    count+=1
  temp[k] = count
print(temp)

# Find divisors of a number
j = 10  #{10:[1,2,5,10]}
temp=[]
for i in range(1,j+1):
  if j%i==0:
    temp.append(i)

tem = {}
tem[j]=temp
print(tem)

# Find divisors for each element in list
l = [10,20,30]
old={}
for i in l:
  new = []
  for j in range(1,i+1):
    if i%j == 0:
      new.append(j)
  old[i]=new
print(old)

# Create nested dictionary with squares and cubes
keys = {}
for i in range(1,4):
  values = {}
  values['s'] = i**2
  values['c'] = i**3
  keys[i] = values

print(keys)

# Classify numbers as even/odd
k=[10,22,21,23]
d = {}
for i in k:
  if i%2==0:
    d[i]='even'
  else:
    d[i]='odd'
print(d)

# Zip keys and values to create dictionary
key=['name','age','city']
value=['john',25,'new york']

temp ={}
for i in range(len(key)):
    temp[key[i]] = value[i]
print(temp)

for a,b in zip(key,value):
  temp[a]=b
print(temp)

print(dict(zip(key,value)))

# Check prime numbers and store in dictionary
j=[11,12,13,14,17]
temp = {}
for i in j:
  count = 0
  for k in range(1,i):
    if i%k==0:
      count+=1
  if count == 1:
    temp[i]='prime'
  else:
    temp[i]='not prime'
print(temp)

# Create dictionary of even squares
temp = {}
for i in range(1,11):
  if i%2==0:
    temp[i]=i**2
print(temp)

# Count character frequency in string
d = 'success' #{s:3,u:1,c:2,e:1}
res = {}

for i in d:
  if i not in res:
    res[i]=1
  else:
    res[i]+=1
print(res)



