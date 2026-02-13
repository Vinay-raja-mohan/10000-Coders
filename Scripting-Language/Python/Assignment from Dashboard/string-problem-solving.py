# Problem 1: Convert string to int without int() function
s = "123"
result = 0
for char in s:
    result = result * 10 + (ord(char) - ord('0'))
print(result)  # 123


# Problem 2: Convert word to title case without title() function
word = "hello world"
title = ""
capitalize = True
for char in range(len(word)):
    if word[char-1] ==" " or char == 0:
        title+=word[char].upper()
    else:
        title+=word[char]

print(title)  # Hello World
