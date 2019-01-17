# src/ExceptionHandling.py
# Fehler- und Ausnahmebehandlung

# Abfangen des ZeroDivisionError
try:
    a, b = 5, 0
    res = a/b
except ZeroDivisionError as e:
    print("error message: ", e)
    print("Das Programm wird beendet.")
else:
    print("Ergebnis: " + str(res))

# Ausgabe:
# error message:  division by zero
# Das Programm wird beendet.



# Abfangen des ZeroDivisionError
# else
try:
    a, b = 5, 2
    res = a / b
except ZeroDivisionError as e:
    print("error message: ", e)
    print("Das Programm wird beendet.")
else:
    print("Ergebnis: " + str(res))

# Ausgabe:
# Ergebnis: 2.5



# finally Nutzung
try:
    file = open("datei.txt", "w")
    a, b = 5, 2
    res = a / b
    file.write("Ergebnis: " + str(res))
except ZeroDivisionError as e:
    print("error message: ", e)
    print("Das Programm wird beendet.")
except FileNotFoundError as e:
    print("error message: ", e)
    print("Das Programm wird beendet.")
else:
    print("Es ist kein Fehler aufgetreten.")
    print("Ergebnis: " + str(res))
finally:
    file.close()
    print("Die Datei wurde geschlossen.")

# Ausgabe auf der Konsole:
# Es ist kein Fehler aufgetreten.
# Ergebnis: 2.5
# Die Datei wurde geschlossen.
