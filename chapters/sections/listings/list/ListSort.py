# lexikographisches Sortieren
liste = ["b", "c", "a"]
print(liste)
liste.sort()
print(liste)

# sortieren nach Zahlenwert
liste = [6, 1, 2, 3, 4, 5]
print(liste)
liste.sort()
print(liste)

# umkehren der Sortierreihenfolge
liste.sort(reverse=True)
print(liste)

# sortieren nach der Laenge einzelner Objekte
liste = ["aa", "aaa", "a"]


def sortFunc(x):
    return len(x)


liste.sort(key=sortFunc)
print(liste)

# umkehren der Sortierreihenfolge
liste.sort(reverse=True, key=sortFunc)
print(liste)