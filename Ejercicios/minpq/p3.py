import config

from DISClib.ADT import minpq as pq
from DISClib.ADT import queue

"""
Simluacion

Cada hora llega un paciente a una cola, cada paciente dura 1.5 horas en ser atendido
¿De que longitud es la cola despues de 5 horas?
"""

def greater(key1, key2):
    if key1['t'] == key2['t']:
        return 0
    elif key1['t'] < key2['t']:
        return -1
    else:
        return 1


cola_de_espera = queue.newQueue()

minpq = pq.newMinPQ(greater)
pq.insert(minpq, {'t': 0, 'evento': 'llegada'})
pq.insert(minpq, {'t': 5, 'evento': 'fin'})


iters = 0
while not pq.isEmpty(minpq) and iters < 100:
    p = pq.delMin(minpq)

    if p['evento'] == 'llegada':
        queue.enqueue(cola_de_espera, 1)
        pq.insert(minpq, {'t': p['t'] + 1, 'evento': 'llegada'})
        print('llegada')
    
    if p['evento'] == 'fin':
        break
    iters = iters + 1

print(queue.size(cola_de_espera))






