# # ALL PYTHON DICTIONARY METHODS (COPY–PASTE READY)

# d = {'a': 1, 'b': 2}

# # clear() → removes all key–value pairs
# d.clear()                          # {}

# # copy() → returns a shallow copy
# d2 = d.copy()                      # {'a': 1, 'b': 2}

# # fromkeys() → creates dictionary from keys with same value
# new_dict = dict.fromkeys(['x','y','z'], 0)   # {'x': 0, 'y': 0, 'z': 0}

# # get() → safely get value (no error if key missing)
# d.get('a')                         # 1

# # items() → returns key–value pairs
# d.items()                          # dict_items([('a',1), ('b',2)])

# # keys() → returns all keys
# d.keys()                           # dict_keys(['a','b'])

# # values() → returns all values
# d.values()                         # dict_values([1,2])

# # pop() → removes key and returns its value
# d.pop('a')                         # 1

# # popitem() → removes and returns last inserted item
# d.popitem()                        # ('b', 2)

# # setdefault() → returns value if key exists, else inserts key with value
# d.setdefault('c', 3)               # 3

# # update() → adds/updates multiple key–value pairs
# d.update({'d': 4})                 # {'a':1,'b':2,'d':4}


# # -------- IMPORTANT DICTIONARY OPERATIONS --------

# # add / update key
# d['e'] = 5

# # access value
# d['e']                             # 5

# # delete key
# del d['e']

# # check key existence
# 'e' in d                           # True / False

# # length of dictionary
# len(d)

# # iterate over keys
# for k in d:
#     print(k)

# # iterate over values
# for v in d.values():
#     print(v)

# # iterate over key–value pairs
# for k, v in d.items():
#     print(k, v)
  
# std_re = [
#     {'std_id':101,'std_name':'kumar','std_age':14},
#     {'std_id':102,'std_name':'sai','std_age':15},
#     {'std_id':103,'std_name':'mohan','std_age':13}
# ]

# for x in std_re:
#     if x['std_id']==101:
#         for k,v in x.items():
#             print(k,'==',v)

# l=[]

# for i in range(3):
#     new={}
#     key = input("give new key: ")
#     value = int(input("give new value: "))
#     new[key] = value
#     l.append(new)

# print(l)
   
    
    
    