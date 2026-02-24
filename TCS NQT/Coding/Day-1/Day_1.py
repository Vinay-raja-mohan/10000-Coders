n = 3
for i in range(n):
  for j in range(n):
    print("*",end=" ")
  print()

print("------------------------------")

# -----------------------------------------------

for i in range(n):
  for j in range(n):
    print(j+1,end=" ")
  print()
print("------------------------------")

# -----------------------------------------------

count = 1
for i in range(n):
  for j in range(n):
    print(count,end=" ")
    count +=1
  print()
print("------------------------------")

# -----------------------------------------------

for i in range(n):
  for j in range(n):
    print(i+1,end=" ")
  print()
print("------------------------------")

# -----------------------------------------------

alph = 65
for i in range(n):
  for j in range(n):
    print(chr(alph),end=" ")
  print()
print("------------------------------")

# -----------------------------------------------

for i in range(n):
  for j in range(65,68):
    print(chr(j),end=" ")
  print()
print("------------------------------")

# -----------------------------------------------

for i in range(n):
  for j in range(n):
    print(chr(alph),end=" ")
    alph+=1
  print()
print("------------------------------")

# ----------------------------------------------- 

for i in range(1,n+1):
  for j in range(i):
    print("*",end=" ")
  print()
print("------------------------------")

# -----------------------------------------------

for i in range(n,0,-1):
  for j in range(i):
    print("*",end=" ")
  print()
print("------------------------------")

# -----------------------------------------------
a=3
for i in range(n):
  for j in range(i):
    print(" ",end=" ")
  
  for j in range(a):
    print("*",end =' ')
  print()
  a-=1
print("------------------------------")

# -----------------------------------------------
a=0
b=3
for i in range(n,0,-1):
  for j in range(i):
    print("*",end=" ")
  

  for j in range(a):
    print("a",end=" ")  
  a+=1  

  for j in range(a):
    print("b",end=" ")

  for j in range(b):
    print("*",end=" ")
  b-=1

  print()