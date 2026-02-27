# print between prime numbers
l=[x for x in range(10,20) if all(x%y!=0 for y in range(2,x))]
print(l)

n=11
l=['prime' if all(n%x!=0 for x in range(2,n)) else 'not prime']
print(l)

l=[x for x in range(1,n) if n%x==0]
if len(l) == 1:
  print('prime')
else:
  print("not prime")

k = ["data.csv","report.pdf","image.pdf"]
res = [x.split('.')[-1]for x in k]
print(res)

# print numbers that are palindrome between range

k=[]
for i in range(100,200):
  temp=i
  sum =0
  while i>0:
    ld = i%10
    i//=10
    sum=sum*10+ld

  if sum == temp:
    k.append(temp)

print(k)

l=[x for x in range(100,200) if str(x)==str(x)[::-1]]
print(l)

# print x!=y in a from of tuple in the res list

x=[1,2,3]
y=[3,1,4]

l=[(i,j) for i in x for j in y if i!=j]
print(l)

# flattern the list
a =[[1,2,3],[10,20,30],[100,200,300]]
l=[y for x in a for y in x]
print(l)

# print all divisible by 2,3
l=[i for i in range(1,20) if i%2==0 or i%3==0]
print(l)

# tuple comprehension
a= (x for x in range(10))
for i in a:
  print(i)

# cube of the odd number in a tuple
a=tuple(((x,x**3) for x in range(1,15) if x%2!=0))
print(a)

# 10 factors using tuple comprehension
n=10
a = tuple((x for x in range(1,n) if n%x==0))
print(a)

# extract vowels from string "comprehension"
a ="comprehension"
a = tuple((x for x in a if x in 'aeiou'))
print(a)

# create tuple from list with len >3
a = ['cat','dog','parrot','cow']
l = tuple((x for x in a if len(x)>3))
print(l)

# ascii values of 'python'
a ='python'
t = tuple(((x,ord(x)) for x in a))
print(t)

# numbers divible by both 3 and 5 from 1-20
t = tuple(x for x in range(1,20) if x%3==0 and x%5==0)
print(t)

# tuple of sqr of numbers from 1,15
t= tuple((x,x**2) for x in range(1,20))
print(t)

# tuple from 50 to 100
t = tuple(x for x in range(50,100) if x%2==0)
print(t)

# 