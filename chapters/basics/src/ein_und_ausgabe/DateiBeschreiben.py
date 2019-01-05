# listings/DateiBeschreiben.py
# Beschreiben einer Datei

datei = open("Daten.txt", "w")

liste = list([42,55,6])
count = 1
for x in liste:
    if count == len(liste):
        datei.write(str(x))
    else:
        datei.write(str(x) + ", ")
    count += 1

datei.write("\nDatei erfolgreich beschrieben!")
datei.close()