import config

from DISClib.ADT import minpq as pq
# from DISClib.Algorithms.Sorting import heapsort

"""
Ordenar con HeapSort unas noticias por fecha
"""

def greater(key1, key2):
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1
