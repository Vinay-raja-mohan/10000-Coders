n =7
# for i in range(n):
#   for j in range(n-i):
#     print(" ",end="")
#   for j in range(i):
#     if j==0  or j==i-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
  
#   print()

# for i in range(n-2,-1,-1):
#   for j in range(n-i):
#     print(" ",end="")
#   for j in range(i):
#     if j==0  or j==i-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
  

#   print()


# for i in range(n):
#   for j in range(n):
#     if j ==0 or j == i-1:
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

# for i in range(n-2,-1,-1):
#   for j in range(i):
#     if j ==0 or j == i-1:
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

for i in range(n):
    for j in range(n*2):
      if  j ==i or j==0 or j==2*n-i-1 or j == 2*n-1:
        print("*",end=" ")
      else:
        print(" ",end=" ")

    print()

for i in range(n-2,-1,-1):
    for j in range(n*2):
      if  j ==i or j==0 or j==2*n-i-1 or j == 2*n-1:
        print("*",end=" ")
      else:
        print(" ",end=" ")

    print()