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

