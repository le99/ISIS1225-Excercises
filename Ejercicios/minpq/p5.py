import config

from DISClib.ADT import indexminpq as pq
from DISClib.ADT import queue

"""
Se tienen N logs de computadores ordenados por fecha y se quiere econtrar los 5 Errores mas recientes 
"""

def greater(key1, entry):
    if key1 == entry['key']:
        return 0
    elif key1 < entry['key']:
        return -1
    else:
        return 1

iminpq = pq.newIndexMinPQ(greater)

iminpq = pq.insert(iminpq, 'A', 300)
iminpq = pq.insert(iminpq, 'B', 101)
iminpq = pq.insert(iminpq, 'C', 1000)
iminpq = pq.insert(iminpq, 'D', 500)

print(pq.delMin(iminpq))

pq.decreaseKey(iminpq, 'D', 200)
pq.increaseKey(iminpq, 'A', 202)

print(pq.delMin(iminpq))


