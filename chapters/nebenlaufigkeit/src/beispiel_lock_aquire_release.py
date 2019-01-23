import threading

lock = threading.Lock()

lock.aquire()
try:
    # kritischer Code
finally:
    lock.release()

with lock:
    # kritischer Code
