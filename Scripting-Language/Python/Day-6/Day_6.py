"Arithmetic Operators"

# Addition in Integers
a = 10
b = 5
print(a + b)          # 15
print("----------------")  

# Addition in strings
str1 = "Hello, "
str2 = "World!"
print(str1 + str2)    # Hello, World!
print("----------------")  

# Addition in Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # [1, 2, 3, 4, 5, 6]
print("----------------")  

# Addition in Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)   # (1, 2, 3, 4, 5, 6)
print("----------------")   

# Addition in Sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(*set1, *set2)      # 1 2 3 4 5 6  (order may vary)
print("----------------")   

# Addition in Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print({**dict1, **dict2})   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("----------------")      

# Multiplication in Integers
x = 4
y = 3
z = x * y
print(z)                  # 12
print("----------------")   

# Multiplication in Strings and integers
str3 = "Hi! "
n = 3
print(str3 * n)           # Hi! Hi! Hi! 
print("----------------")   

# Multiplication in Strings
# str4 = "Na"
# str5 = "Batman!"
# print(str4 * str5)
# print("----------------")   # This will raise an error as multiplication is not defined between two strings

# Multiplication in Lists and integers
list3 = [7, 8, 9]
n2 = 2
print(list3 * n2)         # [7, 8, 9, 7, 8, 9]
print("----------------")    

# Multiplication in Tuples and integers
tuple3 = (10, 11)
n3 = 3
print(tuple3 * n3)        # (10, 11, 10, 11, 10, 11)
print("----------------")    

# Multiplication in Sets and integers
# set3 = {12, 13}
# n4 = 2
# print(set3 * n4)          # This will raise an error as multiplication is not defined for sets
# print("----------------")


# # Multiplication in Dictionaries and integers
# dict3 = {'x': 10}
# n5 = 2
# print(dict3 * n5)         # This will raise an error as multiplication is not defined for dictionaries
# print("----------------")

# Note: Multiplication is not defined for sets and dictionaries in Python, hence those lines will raise errors if uncommented.


#Subtraction in Integers
m = 20
n = 8
print(m - n)             # 12
print("----------------")

# Subtraction in other data types
# str6 = "Hello"
# str7 = "World"
# print(str6 - str7)      # This will raise an error as subtraction is not defined for strings

#Division in Integers
p = 15
q = 3
print(p / q)             # 5.0
print("----------------")

#Floor Division in Integers
r = 17
s = 3
print(r // s)           # 5 this weill give the quotient without decimal
print("----------------")

#Exponentiation in Integers
t = 2
u = 3
print(t ** u)          # 8
print("----------------")


# Modulus in Integers
v = 20
w = 6
print(v % w)          # 2 gives the remainder
print("-----------------------------------------------------------------------------")

# Modulus in other data types
# str8 = "Hello"
# str9 = "World"
# print(str8 % str9)    # This will raise an error as modulus is not defined for strings


"Assignment Operators"

#+=
x1 = 5
x2 = 10
x1 += x2
print(x1)              # 15
print("----------------")

#-=
y1 = 20
y2 = 8
y1 -= y2
print(y1)              # 12
print("----------------")

#*=
z1 = 4
z2 = 3
z1 *= z2
print(z1)              # 12
print("----------------")

#/=
a1 = 15
a2 = 3
a1 /= a2
print(a1)              # 5.0
print("----------------")

#//=
b1 = 17
b2 = 3
b1 //= b2
print(b1)              # 5
print("----------------")

#**=
b1 = 2
b2 = 3
b1 **= b2
print(b1)              # 8
print("----------------")

#%=
b1 = 20
b2 = 6
b1 %= b2
print(b1)              # 2
print("-----------------------------------------------------------------------------")


#Membership Operators"
# in
my_list = [1, 2, 3, 4, 5]
res = 3 in my_list
print(res)             # True
print("----------------")

v = 'hello'
res2 = 'z' in v
print(res2)           # False
print("----------------")

# not in
my_dict = {'a': 1, 'b': 2}
res3 = 'c' not in my_dict
print(res3)           # True
print("----------------")

w = 'world'
res4 = 'o' not in w
print(res4)           # False
print("-----------------------------------------------------------------------------")


"Identity Operators"
# is
a = [1, 2, 3]
b = a
print(a is b)         # True
print("----------------")

c = 500
d = 500
print(c is d)         # False
print("----------------")

# is not
e = 500
f = 500
print(e is not f)     # True
print("----------------")

g = [4, 5, 6]
h = g
print(g is not h)     # False

i = [10,20,30]
j = [10,20,30]
print(i is not j)     # True
print("-----------------------------------------------------------------------------")