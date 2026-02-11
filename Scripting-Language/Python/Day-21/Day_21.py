'set datatype'
a = {1, 2, 3}
b = {3, 4, 5}

print("Initial a:", a)        # Initial a: {1, 2, 3}
print("Initial b:", b)        # Initial b: {3, 4, 5}

# add() → add ONE element
a.add(4)
print("After adding 4 to a:", a)   # {1, 2, 3, 4}

# update() → add MULTIPLE elements
a.update([5, 6])
print("After updating a with [5, 6]:", a)  # {1, 2, 3, 4, 5, 6}

# remove() → remove element (error if not present)
a.remove(2)
print("After removing 2 from a:", a)  # {1, 3, 4, 5, 6}

# discard() → remove element safely (no error)
a.discard(10)
print("After discarding 10 from a:", a)  # {1, 3, 4, 5, 6}

# pop() → remove & return RANDOM element
removed = a.pop()
print("After popping element", removed, "from a:", a)
# remaining elements after pop

# union() → combine both sets (does NOT modify a)
print("Union of a and b:", a.union(b))  # {3, 4, 5, 6}
# other form → print(a | b)

# intersection() → common elements
print("Intersection of a and b:", a.intersection(b))  # {3, 4, 5}
# other form → print(a & b)

# difference() → elements in a but NOT in b
print("Difference of a and b (a - b):", a.difference(b))
# other form → print(a - b)

# symmetric_difference() → elements not common
print("Symmetric difference of a and b:", a.symmetric_difference(b))
# other form → print(a ^ b)

# intersection_update() → keep ONLY common elements
c = a.copy()
c.intersection_update(b)
print("After intersection_update on c:", c)
# other form → c &= b

# difference_update() → remove b elements from a
d = a.copy()
d.difference_update(b)
print("After difference_update on d:", d)
# other form → d -= b

# symmetric_difference_update() → keep non-common elements
e = a.copy()
e.symmetric_difference_update(b)
print("After symmetric_difference_update on e:", e)
# other form → e ^= b

# copy() → create duplicate set
f = a.copy()
print("Copy of a (f):", f)

# isdisjoint() → check if no common elements
print("Is a disjoint with {10,11}?", a.isdisjoint({10, 11}))  # True

# issubset() → check if all elements exist in a
print("Is {3} subset of a?", {3}.issubset(a))  # True
# other form → print({3} <= a)

# issuperset() → check if a contains all elements
print("Is a superset of {3}?", a.issuperset({3}))  # True
# other form → print(a >= {3})

# clear() → remove all elements
a.clear()
print("After clearing a:", a)  # set()


