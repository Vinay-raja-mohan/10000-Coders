"Print sum of even,odd , prime digits in a number "
num = 123456789
e_sum=0
o_sum=0
p_sum=0

while num>0:
  last_dig = num %10
  num//=10
  if last_dig%2==0:
    e_sum+=last_dig
  else:
    o_sum+=last_dig
  temp = 0
  i = 1
  while i<=last_dig:
    if last_dig%i==0:
      temp+=1
    i+=1
  if(temp==2):
    p_sum+=last_dig
  

print(e_sum,o_sum,p_sum)