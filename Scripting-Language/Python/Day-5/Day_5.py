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
