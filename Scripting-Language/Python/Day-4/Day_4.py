"Tuple DataType"

l = ()
m = tuple()
n = 1, 2, 3, 4, 5
o = 'a',
t = (10,'python',3.2,True,2+3j,[10,20,30]) #tuple with different data types

print(type(l))  #tuple
print(type(m))  #tuple
print(type(n))  #tuple
print(type(o))  #tuple
print(type(t))  #tuple
print(t[1:4])  #slicing
print(t[-1])   #accessing last element

"Set DataType"

k = {20}
print(type(k))  #set

k={'vinay','vinay','kumar',20,30,20.5,30} #set with different data types and duplicate values
print(k)  #duplicates will be removed


"Dictionary DataType"
d = {}
d1 = dict()
d2 = {'name':'vinay','age':22,'course':'python'}
print(d2['name']) #accessing value using key
d2['age'] = 23  #modifying value
