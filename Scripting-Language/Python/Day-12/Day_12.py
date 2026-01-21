"Nested For Loops - Star Patterns"

# for row in range(1,6):
#   for col in range (1,6):
#     print("* ",end="")
#   print()

# for i in range(2,10):
#   for x in range(i):
#     print(x,end="")
#   print()

# for i in range(1,6):
#   for j in range(1,i+1):
#     print(j,end=" ")
#   print()

# for i in range(5):
#   temp = 64
#   for j in range(i+1):
#     temp+=1
#     print(chr(temp),end=" ")
#   print()

# for i in range(6,0,-1):
#   for j in range(i):
#     print(j,end=" ")
#   print()

"While Loop"
# a=0
# while a<10:
#   print(a,end=" ")
#   a+=1

# a=-1
# while a>=-10:
#   print(a,end=" ")
#   a-=1

# a=-10
# while a<=-1:
#   print(a,end=" ")
#   a+=1

# j=121
# temp=j
# sum=0
# while j>0:
#   a=j%10
#   sum=sum*10+a
#   j=j//10
# print(sum)

# if(temp==sum):
#   print("Palindrome")

j = 23456
sum=0
while j>0:
  d = j%10
  j//=10


  if(d%2==0):
    sum+=d
print(sum)