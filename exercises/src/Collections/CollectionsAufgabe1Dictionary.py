dictionary = dict(A="Alpha", L="Lima", E="Echo", X="Xray")
print(dictionary)


print(dictionary.values())

dictionary1 = dict(N="November", A="Alpha", T="Tango", O="Oscar" )
dictionary2 = {}

for d in (dictionary, dictionary1):
    dictionary2.update(d)

print(dictionary2)