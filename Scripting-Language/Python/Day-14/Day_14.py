# "Palindrome using while loop"
# a = 121
# temp = a
# sum=0

# while a > 0:
#   digit = a % 10
#   sum = sum * 10 + digit
#   a//=10
# if (temp==sum):
#   print("palindrome")
# else:
#   print("Not Palindrome")


# "Between Palindrome"

# for num in range(100,150):
#   temp = num
#   sum=0
#   while num > 0:
#     digit = num % 10
#     sum = sum * 10 + digit
#     num//=10
#   if (temp==sum):
#     print(temp,"is palindrome")
#   else:
#     print(temp,"is Not Palindrome")

# "Fibbinocci Series"
# n =1
# a,b = 0,1
# while n<=10:
#   print(a,end = " ")
#   a,b=b,a+b
#   n+=1

# "Max Digit from a number"
# a = 12934
# temp = 0
# while a > 0:
#   digit = a %10
#   a//=10
#   if (digit > temp):
#     temp = digit
# print (temp)


# "Min Digit From a number"
# b = 129340
# temp = 10
# while b > 0:
#   digit = b%10
#   b//=10
#   if (digit < temp):
#     temp = digit
# print (temp)

# "Nested While Loop"
# a = 1
# while a <= 5:
#   b=0
#   while b < a:
#     print("*",end = " ")
#     b+=1
#   a+=1
#   print()

# "5 - 8 Tables using nested while loop"
# a= 5
# while a<=8:
#   b = 1
#   while b <=10:
#     print(f"{a} x {b} = {a*b}")
#     b+=1
#   a+=1
#   print()

"printing each alphabet individually"

h = "python"
i = 0
while i < len(h):
  if(h[i] in "aeiouAEIOU"):
    print(h[i])
  i+=1

