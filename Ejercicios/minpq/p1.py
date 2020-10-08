import config

from DISClib.ADT import minpq as pq

"""
Encontrar los 5 elementos mas pequeños de un lista
"""

def greater(key1, key2):
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1


minpq = pq.newMinPQ(greater)


pq.insert(minpq, 5)
pq.insert(minpq, 23)
pq.insert(minpq, 31)
pq.insert(minpq, 15)

print(pq.delMin(minpq))
print(pq.delMin(minpq))
print(pq.delMin(minpq))




