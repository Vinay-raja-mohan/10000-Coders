# Problem 1: Check prime and multiply with 2
numbers = [10, 30, 50, 20, 7, 11, 13]
result = []
for num in numbers:
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        result.append(num * 2)
    else:
        result.append(num)
print(result)


# Problem 2: Sort list in ascending order without sort function
lst = [10, 30, 50, 20]
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)


# Problem 3: Check if list is in ascending order
arr = [10, 30, 50, 20]
is_ascending = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_ascending = False
        break
if is_ascending:
    print("ascending order")
else:
    print("non-ascending order")
