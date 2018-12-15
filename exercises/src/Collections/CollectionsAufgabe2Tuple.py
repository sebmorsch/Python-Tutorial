t1 = (2, 3)
tmpList = list(t1)
tmpList.append(4)
tmpList.append(5)
t1 = tuple(tmpList)
print(t1)

x = ("hallo", 1, 2.1, False, "string")
y = []
for i in x:
    y.append(str(i))

x = tuple(y)
print(x)

for i in x:
    print(type(i) is str)
