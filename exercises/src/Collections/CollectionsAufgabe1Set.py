set1 = set((4, 5, 6))
print(set1)
set2 = set((3,4,5))
print(set2)



print (set1 & set2)


set3 = set1.union(set2)
print(set3)


set3.add(7)
set3.add(4) #Error
print(set3)

