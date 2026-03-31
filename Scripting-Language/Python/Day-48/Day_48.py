# without changing the code we change the functionality of the code then it is a decorators function.

# def good(wish):
#   def inner():
#     print("Bad Morning")
#     wish()
#   return inner


# @good  #decorator
# def wish():
#   print("Good Morning")

# wish()

# def prime(fun):
#   def inner():
#     for i in range(10,30):
#       for j in range(2,i):
#         if i%j==0:
#           break
#       else:
#         print(i)
#   return inner

# @prime
# def fun():
#   for x in range(10,30):
#     print(x)

# fun()

# def even(chck):
#   def inner(b):
#     if b%2==0:
#       print('even')
#     else:
#       print("odd")
#   return inner

# @even
# def check_number(a):
#   print(a)

# check_number(10)


# def prime(num):
#   def inner(a,b):
#     for i in range(a,b):
#       for j in range(2,i):
#         if i%j==0:
#           break
#       else:
#         print(i)
#   return inner


# @prime
# def num(a,b):
#   print(a,b)

# num(20,30)

# def cred(log):
#   def inner(usr,pas):
#     a = input('enter username : ')
#     b = input("enter password : ")
#     if a == usr:
#         if b == pas:
#             print("Login successful")
#         else:
#             print("Password is wrong")
#     else:
#       print("Check your credentials")
#   return inner



# @cred
# def log(username,password):
#   print(username)
#   print(password)

# log('vin','123')


# import time
# def timer(fun):
#   def inner():
#     s=time.time()
#     fun()
#     e = time.time()
#     print(e-s)
#   return inner


# @timer
# def fun():
#   for x in range(10):
#     pass  

# fun()

def deco1(fun):
  def inner():
    print("First decorator")
    # fun()
  return inner

def deco2(fun):
  def inner():
    print("Second decorator")
    fun()
  return inner

@deco1
@deco2
def fun():
  print('------multiple decorators------')


fun()