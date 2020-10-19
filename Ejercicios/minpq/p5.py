import config

# from DISClib.ADT import indexminpq as pq
from DISClib.DataStructures import indexminpq as pq
from DISClib.ADT import queue

"""
Se tienen N logs de computadores ordenados por fecha y se quiere econtrar los 2 Errores mas recientes 
"""

logs = [
    [
        {'t': 1, 'm': 'Error'},
        {'t': 4, 'm': 'Error'},
        {'t': 7, 'm': 'm'},
    ],
    [
        {'t': 2, 'm': 'm'},
        {'t': 5, 'm': 'Error'},
        {'t': 8, 'm': 'm'},
    ],
    [
        {'t': 3, 'm': 'm'},
        {'t': 6, 'm': 'Error'},
        {'t': 9, 'm': 'm'},
    ]
]


def greater(k1, k2):
    if k1['t'] == k2['t']:
        return 0
    elif k1['t'] > k2['t']:
        return -1
    else:
        return 1



iminpq = pq.newIndexMinPQ(len(logs), greater)

for i, log in enumerate(logs):
    pq.insert(iminpq, i, log.pop())


num_err = 0

while not pq.isEmpty(iminpq):
    minLog = pq.minKey(iminpq)
    minI = pq.delMin(iminpq)

    if len(logs[minI]) > 0:
        log = logs[minI].pop()
        pq.insert(iminpq, minI, log)

    if minLog['m'] == 'Error':
        print(minLog)
        num_err = num_err + 1
        if num_err == 2:
            break




