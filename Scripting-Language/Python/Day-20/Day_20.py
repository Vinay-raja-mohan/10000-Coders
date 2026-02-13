# Check if list is in ascending order
k = [10,10,12,13,14]
is_ascending = True
for i in range(len(k)-1):
  if k[i+1]<k[i]:
    is_ascending = False
    break

if is_ascending:
  print("Ascending")
else:
  print("Not Ascending")

# Calculate average of list
k = [10,20,30,40]
sum=0
count=0
for i in k:
  sum+=i
  count+=1
print(sum/count)

# Sort list using bubble sort
l = [10,11,12,13,14,9]
for i in range(len(l)):
  for j in range(i+1,len(l)):
    if l[j]<l[i]:
      l[i],l[j]=l[j],l[i]
print(l)

# Find pairs that sum to target value
k = [1,2,3,4,5,6,7,8]
for i in range(len(k)):
  for j in range(i+1,len(k)):
    if k[i]+k[j] == 10:
      print (k[i],k[j])

# Remove duplicates from list
k=[10,11,12,13,10]
temp = []
for i in k:
  if i not in temp:
    temp+=[i]
print(temp)

# Check if list elements are unique
is_unique = True
for i in range(len(k)):
  for j in range(i+1,len(k)):
    if k[i]==k[j]:
      is_unique = False
      break
if is_unique:
  print("Unique")
else:
  print("Not Unique")

# Find second maximum element
k=[10,12,13,15,15]
temp=[]
for i in range(len(k)):
  for j in range(i+1,len(k)):
    if k[i]>k[j]:
      k[i],k[j]=k[j],k[i]
maxi = k[-1]
tem = 0
for l in k:
  if l>tem and l<maxi:
    tem = l
print(tem)

# Find second minimum element
k = [10,11,12,13,14]

min1 = min2 = float('inf')

for i in k:
    if i < min1:
        min2 = min1
        min1 = i
    elif i < min2 and i != min1:
        min2 = i

print(min2)

# Replace negative numbers with 0
k = [10,-12,-8,-9,13,14]
for i in range(len(k)):
  if k[i] < 0:
    k[i]=0
print(k)

# Sort list with 0s and 1s
k=[1,0,1,0,1,0,1,0]
for i in range(len(k)):
  for j in range(i+1,len(k)):
    if k[i]>k[j]:
      k[i],k[j]=k[j],k[i]
print(k)

# Separate positive and negative numbers
k=[10,-2,-3,11,13,-4]
pos = []
neg = []
for i in k:
  if i<0:
    neg+=[i]
  else:
    pos+=[i]
print(pos,neg)

# Flatten list of lists
k=[[10,20,30],[100,200,300,400]] #[10,20,30,100,200,300,400]
temp=[]
for i in k:
  for j in i:
    temp+=[j]
print(temp)

# Flatten nested list with mixed types
k=[10,20,30,[100,200,300,400]] #[10,20,30,100,200,300,400]
temp =[]
for i in k:
  if type(i) != int:
    temp.extend(i)
  else:
    temp.append(i)
print(temp)