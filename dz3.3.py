lst = [1, 2, 3, 4, 5, 6, True, "popa", 3.1415]
mid = (len(lst)+1) // 2
first = lst[:mid]
second = lst[mid:]
result = [first,  second]
print(result)