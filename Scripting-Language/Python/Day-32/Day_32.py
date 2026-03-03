# even or odd using dict comprehension
res = (10,11,12,13,14,15,16)
temp = { x:'even' if x%2==0 else 'odd' for x in res}
print(temp)

# sqaure and cube values
d = {x:{'s':x**2,'c':x**3} for x in range(1,10)}
print(d)

# number with its factors
h =[10,12,8,15]
d = {x:[y for y in range(1,x) if x%y==0]  for x in h}
print(d)

res = {}
for x in h:
  temp =[]
  for y in range(1,x):
    if x%y ==0:
      temp.append(y)
  res[x] = temp
print(res)

# prime and not prime
j = [11,12,13]
ress = {i:'prime' if all(i%k!=0 for k in range(2,i)) else 'not prime'for i in j}  
print(ress)

# len > 3 print from list and thier len too
l = ['vina','hi','hello','is','taraka','venkata']
res = {x:len(x) for x in l if len(x)>3}
print(res)

# values > 50
l = {'a':50,'b':60,'c':30,'d':40}
res = {k:v for k,v in l.items() if v> 50}
print(res)


# even and odd
a = [0,1,2,3,4,5,6,1]
res = {'even':[x for x in a if x%2==0],'odd':[x for x in a if x%2!=0]}
print(res)


eve = []
odd =[]
temp ={}
for i in a:
  if i%2==0:
    temp.setdefault('even',[]).append(i)
  else:
    temp.setdefault('odd',[]).append(i)
print(temp)


# reverse the string and print it in the dict
a=['cat','dog','bat']
res = {x:x[::-1] for x in a}
print(res)

# tables in dict
res = {i:[i*j for j in range(1,11)] for i in range(1,4)}
for k, v in res.items():
    print(k, ":", v)
