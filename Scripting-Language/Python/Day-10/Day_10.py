"Loops"
a = 'for_loop'

for i in range(len(a)):
    print(a[i])

s = "while_loop"

for x in s:
    print(x)

t = [1,2,{'a':10, 'b':20},(5,6,7),{'a','b','c'}]

for item in t:
    print(item)

b = {1,2,3,4,5,'hello',6}
for num in b:
    print(num)

c = {'name':'Alice', 'age':30, 'city':'New York'}
for key in c:
    print(key, c[key])