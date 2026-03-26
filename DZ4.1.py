lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
ne_null = []
null = []
for x in lst:
    if x == 0:
        null.append(x)
    else:
        ne_null.append(x)
result = ne_null + null
print(result)
