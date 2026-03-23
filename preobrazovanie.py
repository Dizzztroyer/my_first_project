lst1 = []      #прикольно, не сразу додумался тут if использовать и длину
if len(lst1) <= 1:
    lst2 = lst1
else:
    lst2 = [lst1[-1]] + lst1[:-1]
print(lst2)