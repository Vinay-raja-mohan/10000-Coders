"Nested For Loops In Python"

for i in range(1, 4):
    for j in range(1, 4):
        print(f'i = {i}, j = {j}')

print("--------------")

for x in ['A', 'B', 'C']:
    for y in [1, 2, 3]:
        print(f'x = {x}, y = {y}')


print("--------------")


for x in range(20,30):
    count = 0
    for y in range(1,x):
        if x%y == 0:
            count += 1
    
    if count == 1:
        print(f'{x} is a prime number')

print("--------------")

s = ['python', 'java', 'fullstack' , 'c++']

for x in range(0,len(s)):
    if x%2 == 0:
        print(f'Index: {s[x]}')

print("--------------")

for x in s:
    for y in x:
        if y in 'aeiou':
            print(f'Vowel: {y}')
    print()

print("--------------")

for x in s:
    count = 0
    for y in x:
        if y in 'aeiou':
            count += 1
    if count > 1:
        print(f'Word with at least 2 vowels: {x}')

print("--------------")

for i in range(100,150):
    y = str(i)[::-1]
    if(i == int(y)):
        print(f'Palindrome number: {i}')

print("--------------")


for i in range(100,1000):
    length = len(str(i))
    a = 0
    for j in str(i):
        a += int(j)**length
    if a == i:
        print(f'Armstrong number: {i}')