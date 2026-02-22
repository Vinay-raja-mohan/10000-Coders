#  Functions
# Which help us to use a piece of code repetatively

# Types of Functions
#     1.Predefined Functions   --print(),max(),min(),avg(),sum()
#     2.Userdefined Functions


# def even(a,b):
#   for i in range(a,b+1):
#     if i%2==0:
#       print(i)

# even(10,20)
# print("-------")
# even(21,30)


def pos(a):
  if a <0:
    print("neg")
  elif a > 0:
    print("pos")
  else:
    print('zero')
pos(0)