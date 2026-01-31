j = "MakesFirstLetter"

s=0

for i in j:
  s+=1
print(s)

n =''
for x in j:
  if x.isupper():
    n += '_' + x
  else:
    n+=x

print(n)

m=""
for a in n:
  m+=a.strip("_")

print(m)

o = ""
for b in n:
  if b.isalpha():
    o+=b
print(o)


j = "letters"
print(j.count("t"))


l1 = [1,2,3]
l2 = [10,20,30]

print(l1+l2)