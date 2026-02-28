"Dictonary Comprehension"
# sqaures of the number
res = {x:x**2 for x in range(1,4)}
print(res)

# reverse key and value
res = {'a':10,'b':20,'c':30}
r = {v:k for k,v in res.items()}
print(r)

# print even or odd with num
res=[10,11,12,13] # res = {10:'even',11:'odd',12:'even',13:'odd'}
d = {k:"even" if k%2==0 else 'odd' for k in res}
print(d)

# squares and cubes 
r = {x:{'square':x**2,'cube':x**3}for x in range(1,4)}
print(r)

d={}
for x in range(1,4):
  d[x]={'square':x**2,'cube':x**3}
print(d)

# mapping alpha with thier ascii values
res={chr(x):x for x in range(ord('a'),ord('z')+1)}
print(res)

# reverse the input as value
words=['cat','dog','bat']
res ={x:x[::-1] for x in words}
print(res)
