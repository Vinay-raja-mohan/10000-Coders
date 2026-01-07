"Comparison Operators in Python"
a = "ab"
b = 'ba'
print(a == b)        # False
print("---------------------------------------------------------------------")

"Logical Operators"

# and
v1 = 100
v2 = 200
result = v1<v2 and v1!=v2
print(result)          # True
print("----------------")

# or
n=10
if n%2==0 or n%3==0:
    print("Divisible by 2 or 3")   # Divisible by 2 or 3
print("----------------")

# not
a = 100
b = not a>200
print(b)               # True
print("---------------------------------------------------------------------")
