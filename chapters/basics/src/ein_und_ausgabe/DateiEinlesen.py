# listings/DateiEinlesen.py
# Einlesen einer Datei

datei = open("Daten.txt","r")

for line in datei:
    print(line)

datei.close()