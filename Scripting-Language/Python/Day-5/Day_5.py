"Nested Dictionaries in Python"
d={'kumar':{'telugu':85,'hindi':90,'english':88}}
print(d['kumar'])
print(d['kumar']['hindi'])  #accessing nested value
d['kumar']['maths'] = 92  #adding new key-value pair in nested dictionary
print(d['kumar'])

d1 = {'name':'kumar','age':18,'name':'vinay'}  #duplicate keys
print(d1)  #last assignment will be considered

for x in d1:
    print(x)
print("-----")

for x in d1.values():
    print(x)
print("-----")

for x,y in d1.items():
    print(x,y)
print("-----")

print(len(d1))  #length of dictionary

print('----------')

"Operations"

"Operations on Sets"
s1 = {10,20,30,40}
s2 = {30,40,50,60}
for x in s2:
    s1.add(x)  #union operation
print(s1)


"Operations on Tuples"
t1 = (10,20,30)
t2 = (40,50,60)
t3 = t1 + t2  #concatenation
print(t3)

"Operations on Dictionaries"
d3 = {'a':10,'b':20,'c':30}
d4 = {'d':40,'e':50}

for k,v in d4.items():
    d3[k] = v  #merging two dictionaries