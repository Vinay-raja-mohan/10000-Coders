"List Comprehention"

# 1. append in list from 1-6
l=[i for i in range(1,7)]
print(l)

# 2. append in list in list form from 1-6
l=[[i] for i in range(1,7)]
print(l)

# 3. append even number in a list
l = [i for i in range(1,11) if i%2==0]
print(l)

# 4. res=[1,2,5] write query for this res - factors of 10
n =10
l = [i for i in range(1,n) if n%i==0]
print(l)

# 5. print the squares from 1 - 10 in a list
n = 10
l=[(i,i**2) for i in range(1,n+1)]
print(l)

# 6. print the even squares from 1 - 10 in a list
n = 10
l=[(i,i**2) for i in range(1,n+1) if i%2==0]
print(l)

# 7. extract vowels from the string using list
a='python'
l = [i for i in a if i in 'aeiou']
print(l)

# 8. append even for even_no or odd for odd_no in a list
s = [10,11,12,13]
l = ['even'if i%2==0 else 'odd' for i in s]
print(l)

# 9. make it upper case python
l = [i.upper() for i in a]
print(l)

# 10. res = [10,12,8,9] output = [[1,2,5],[1,2,3,4,6],...]
res= [10,12,8,9]
tem =[]
for i in res:
  temp=[]
  for j in range(1,i):
    if i%j==0:
      temp.append(j)
  tem.append(temp)
print(tem)

l=[[j for j in range(1,i) if i%j==0 ]for i in res]
print(l)

# 11. 50-100 ends with digit 5
l=[i for i in range(50,100) if i%10==5]
print(l)

# 12. divisiblr by both 10 and 20
l=[i for i in range(20,100) if i%20==0 and i%10==0]
print(l)

# 13. print prime from a list
i = [11,12,13,14,15]
l = ["prime" if all(x % y != 0 for y in range(2,x)) else "not prime" for x in i]
print(l)

temp = []
for x in i:
  for y in range(2,x):
    if x%y==0:
      temp.append("not prime")
      break
  else:
    temp.append("prime")
print(temp)

# 14. pop the zeros from a list
s=[10,0,20,0,30,0]
l=[i for i in s if i!=0]
print(l)

# 15. key pair addition
a=[10,20,30]
b=[1,2,3]
l=[a[i]+b[i] for i in range(0,len(a))]
print(l)