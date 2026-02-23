"strong number"

def strong(n):
  sum1=0
  while n>0:
    ld = n % 10
    n//=10
    sum =1
    for i in range(1,ld+1):
      sum*=i
    sum1+=sum
  return(sum1)

n=145
new = strong(n)

if new == n:
  print("Strong number")
else:
  print("not a strong number")



def employee(name,id,salary=3000):
  print(salary)

employee('vina',id=2000,salary=101)
