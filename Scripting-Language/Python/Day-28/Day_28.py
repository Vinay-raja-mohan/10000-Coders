"Variable Length Argument"

def add1(a,b):
  print(a+b)

add1(100,200)


# we cant 3 values where there are only 2 paramenters

def vla(*a):                # prints the output in tuple data type
  sum1=0
  for i in range(len(a)):
    if type(a[i]) == int:
      sum1+=a[i]
  print(sum1)    

vla(2)
vla(10,20,'a','b')
vla(10,20,30,40,50)
vla(10,20,30,40,50,60,70,80)


def emp(name,pin,*department,salary =25000):
  print('employee name:' ,name)
  print('employee pin number:',pin)
  print('employee dept:',department)
  print('employee salary:',salary)


emp('sai',101,'it','hr')


"Keyword Variable Length Argument"

def kvla(**a):
  for k,v in a.items():
    print(k,"=",v)

kvla(name='kumar',pin=101,age=15)

def fun(v1,v2,*a,b=25000,**n):
  print('v1: ',v1)
  print('v2: ',v2)
  print('a: ',a)
  print('b: ',b)
  print('n: ',n)

fun(1,2,'a','b',2,3,4,b=30000,name='vinay',m_name='raja',l_name='mohan')


# calculator

def cal(a,b,c):
  if c== '+':
    return(a+b)
  elif c == '-':
    return(a-b)
  elif c == '/':
    return a/b
  elif c =='%':
    return a%b
  elif c == '*':
    return a*b
  else:
    print("invalid operator")


while True:
  a = int(input("enter the first number : "))
  b = int(input("enter the second number : "))
  c = input("enter the operator +, -, /, %, * : ")


  print(cal(a,b,c))

  n = int(input("If exit press 1 : "))

  if n==1:
    break


#sort without sort function in a function

def sort(l):

  for i in range(len(l)):
    for j in range(i+1,len(l)):
      if l[i] > l[j]:
        l[i],l[j]=l[j],l[i]
  print(l)

sort([10,2,3,9,8,7,6])


"Nested Functions"

def out():
  a=20
  print("outer")
  def inner():
    b =30
    print(a+b)

  
  print("after inner")
  inner()

out()


def even():
  s=[]
  for x in range(10,20):
    if x%2==0:
      s.append(x)
  return s

print(even())


def wish():
  print('good morning')
  return 1

print(wish())


def is_prime(a):
  if a<=1:
    return False

  for x in range(2,a):
    if a%x==0:
      return False
  return True


def n_prime(a):
  upper = a
  lower = a
  while True:
    if is_prime(upper):
      return upper
    elif is_prime(lower):
      return lower
    
    upper+=1
    lower-=1


print(n_prime(8))

