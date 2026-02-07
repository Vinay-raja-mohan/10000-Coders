# PYTHON STRING METHODS – SMALL EXAMPLES WITH OUTPUTS

# ---------------- CASE CONVERSION ----------------
print("hello".upper())          # HELLO
print("HELLO".lower())          # hello
print("hello world".title())    # Hello World
print("python language".capitalize())  # Python language
print("PyThOn".swapcase())      # pYtHoN
print("HELLO".casefold())       # hello

# ---------------- SEARCH / FIND ----------------
print("banana".find("na"))      # 2
print("banana".rfind("na"))     # 4
print("apple".index("p"))       # 1
print("apple".rindex("p"))      # 2
print("banana".count("a"))      # 3
print("python".startswith("py"))  # True
print("python".endswith("on"))    # True

# ---------------- CHECKING ----------------
print("Hello".isalpha())        # True
print("1234".isdigit())         # True
print("abc123".isalnum())       # True
print("hello".islower())        # True
print("HELLO".isupper())        # True
print("   ".isspace())          # True
print("Hello World".istitle())  # True

# ---------------- MODIFY / REPLACE ----------------
print("hello world".replace("world","python"))  # hello python
print("  hi  ".strip())         # hi
print("  hi".lstrip())          # hi
print("hi  ".rstrip())          # hi
print("unhappy".removeprefix("un"))   # happy
print("testing.py".removesuffix(".py"))  # testing

# ---------------- SPLIT / JOIN ----------------
print("a b c".split())          # ['a', 'b', 'c']
print("a-b-c".rsplit("-",1))    # ['a-b', 'c']
print("hi\nhello".splitlines()) # ['hi', 'hello']
print("-".join(['a','b','c']))  # a-b-c

# ---------------- ALIGN / FORMAT ----------------
print("hi".center(6,"*"))       # **hi**
print("hi".ljust(5,"-"))        # hi---
print("hi".rjust(5,"-"))        # ---hi
print("7".zfill(3))             # 007
print("My age is {}".format(20)) # My age is 20

# ---------------- ENCODING ----------------
print("hi".encode())            # b'hi'
