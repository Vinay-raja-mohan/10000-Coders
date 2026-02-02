"String functions"
k = "python"
print(k.upper())

print(ord("z"))
print(chr(65))

diff = (ord("a")-ord("A"))
up = ""
for i in k:
  if ord(i) >= 97 and ord(i) <= 122:
    d = ord(i) - 32
    up += chr(d)
print(up)

k = "pYtHoN"
sum = ""
for i in k:
  if ord(i)>=65 and ord(i)<=90:
    d = ord(i) + 32
    sum+= chr(d)
  elif ord(i) >= 97 and ord(i)<= 122:
    d = ord(i) - 32
    sum += chr(d)
print(sum)


i = "support indexing tables"
count = 0
for x in i:
  count +=1

print(count) 
print(i.count("p"))

d = i.split()
print(d)

for x in d:
  print(len(x),end = " ")

for i in k:
  print(i.isupper(),i)



