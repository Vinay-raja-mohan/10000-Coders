# funtions




# modes
# x ==> new file create, write
# w ==> write, create
# r ==> only read
# a ==> create, append


# w+ ==> write,read
# r+ ==> read,write
# a+ ==> append, read

# rb ==> read binary
# wn ==> write binary


# with open('file1.txt','w') as a:
#   a.write("vinay raja mohan")

# d = open('file1.txt','a')
# d.write('\nGelli t n s v')


# with open('file2.txt','w+') as h:
#   h.write("hello this is file 2")
#   h.seek(0)
#   data = h.read()
#   print(data)


# with open('file2.txt','r+') as h:
#   r = h.read()
#   print(r)
#   h.seek(2)
#   h.write('\na b c d')
#   h.seek(0)
#   r = h.read()
#   print(r)


# with open('file2.txt','a+') as v:
#   v.write("\nthis is the last text")
#   v.seek(0)
#   a= v.read()
#   print(a)

# r = open('file1.txt','r')
# print(r.read())
# print()
# r.seek(0)
# a = r.readlines()
# print(len(a))


# print("---")
# r.seek(0)
# le = 0
# for i in r:
#   a = (i.split())
#   le += len(a)
# print(le)


# r.seek(0)
# print(len(r.read().split()))


# r.seek(0)
# z = r.read()
# cou = 0
# for x in z:
#   cou+= 1
# print(cou)


# import os
# if os.path.exists('file2.txt'):
#   os.remove('file2.txt')


def even_decorator(func):
    def wrapper():
        for i in range(10, 21):
            if i % 2 == 0:
                print(i)
        # func()   # call original if needed
    return wrapper


@even_decorator
def print_numbers():
    print("Done printing evens")

print_numbers()


