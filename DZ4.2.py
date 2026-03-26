lst = []
symlst = sum(lst[::2])
if lst == []:
    print(0)
else:
    print(symlst * lst[-1])


#ну или с компрессией, но верхний пока больше нравится( более понятный будто)

lst = []
print(sum(lst[::2])*lst[-1] if lst else 0)