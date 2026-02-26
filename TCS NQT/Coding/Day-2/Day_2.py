"*****"
" *** "
"  *  "
n=3
a=5
for i in range(n):
  for j in range(i):
     print(" ",end="")
  
  for j in range(a):
      print("*",end="")
  
  a-=2
  print()
  
           ****
           *  *
           *  *
           ****
n=5
for i in range(n):
  for j in range(n):
    if i == 0 or i == n-1:
      print("*",end="")

  if i > 0 and i < n-1:
    for j in range(n):
      if j ==0 or j == n-1:
        print("*",end="")
      else:
        print(" ",end="")
  print()

 *******
 a*aaa*
 aa*a*
 aaa*

r = int(input("Enter the number of rows: "))

for i in range(r, 0, -1):   # outer loop (rows)
    
    # spaces before pyramid
    for k in range(r, i, -1):
        print("a", end="")
    
    # stars and spaces
    for j in range(i*2 - 1):
        
        if i == r:                 # first row (full stars)
            print("*", end="")
        
        else:
            if j == 0 or j == i*2 - 2:   # border stars
                print("*", end="")
            else:
                print(" ", end="")
    
    print()   # new line
    

n = 4

for i in range(n):
    for j in range(n-i-1):   # spaces
        print("a", end="")
        
    for j in range(2*i+1):   # stars (odd numbers)
        print("*", end="")
        
    print()

  

      
