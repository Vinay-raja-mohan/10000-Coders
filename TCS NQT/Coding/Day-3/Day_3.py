# # 1 1 1
# #  1 1
# #   1
# n=3
# for i in range(n):
#   for j in range(i):
#     print(" ",end="")
  
#   for j in range(n-i):
#     print("* ",end="")
  
#   print()

# n=3
# for i in range(n):
#   for j in range(n-i-1):
#     print(" ",end="")
#   for j in range(i+1):
#     print("* ",end="")
#   print()

# for i in range(1,n):
#   for j in range(i):
#     print(" ",end="")
#   for j in range(n-i):
#     print("* ",end="")
#   print()

# * a a a a a a * 
# * * a a a a * *
# * * * a a * * *
# * * * * * * * *
# ----------------------
# * * * * * * * *
# * * * a a * * *
# * * a a a a * *
# * a a a a a a *

n=4
for i in range(n):
  for j in range(i+1):
    print("*",end=" ")

  for j in range(n-i-1):
    print(" ",end=" ")
  
  for j in range(n-i-1):
    print(" ",end=" ")

  for j in range(i+1):
    print("*",end=" ")
  print()

for i in range(n):
  for j in range(n-i-1):
    print("*",end=" ")
  for j in range(i+1):
    print(" ",end=" ")
  
  for j in range(i+1):
    print(" ",end=" ")
  for j in range(n-i-1):
    print("*",end=" ")
  print()


n=5
for i in range(n):
  for j in range(n-i-1):
    print(" ",end=" ")
  
  num = 1

  for j in range(i+1):
      print(num, end="   ")
      num = num*(i-j)//(j+1)

  print()

