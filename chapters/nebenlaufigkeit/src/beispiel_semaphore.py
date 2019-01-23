import threading

# Initialisierung der Semaphore
maxconnections = 5
# ...
pool_sema = threading.BoundedSemaphore(value=maxconnections)


# Zugriff auf die Datenbank in den Arbeiterthreads
with pool_sema:
    conn = connectdb()
    try:
        # ... Verbindung nutzen ...
    finally:
        conn.close()
