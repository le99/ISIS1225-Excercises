"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

from DISClib.ADT import map as map
from DISClib.DataStructures import liststructure as lt

"""
Estructura que contiene la información de una cola de prioridad indexada,
orientada a menor

Basada en: 
https://github.com/kevin-wayne/algs4/blob/master/src/main/java/edu/princeton/cs/algs4/IndexMinPQ.java

"""


def newIndexMinPQ(maxN, cmpfunction):
    if maxN < 0:
        raise Exception('maxN must be > 0')
    return {
        'maxN': maxN,
        'keys': [None] * (maxN + 1),
        'pq':   [None] * (maxN + 1),
        'qp':   [-1] * (maxN + 1),
        'n': 0,
        'compare': cmpfunction
    }
def isEmpty(iheap):
    return iheap['n'] == 0

def contains(iheap, i):
    validateIndex(iheap, i)
    return iheap['qp'][i] != -1

def insert(iheap, i, key):
    validateIndex(iheap, i)
    if(contains(iheap, i)):
        raise Exception('Index already exists in pq')
    iheap['n'] = iheap['n'] + 1
    iheap['qp'][i] = iheap['n']
    iheap['pq'][iheap['n']] = i
    iheap['keys'][i] = key
    swim(iheap, iheap['n'])

def minIndex(iheap):
    if n == 0:
        raise Exception('Pq underflow')
    return iheap['pq'][1]

def minKey(iheap):
    if iheap['n'] == 0:
        raise Exception('Pq underflow')
    return iheap['keys'][iheap['pq'][1]]

def delMin(iheap):
    if iheap['n'] == 0:
        raise Exception('Pq underflow')
    min = iheap['pq'][1]
    exch(iheap, 1, iheap['n'])
    iheap['n'] = iheap['n'] - 1
    sink(iheap, 1)
    iheap['qp'][min] = -1
    iheap['keys'][min] = None
    iheap['pq'][iheap['n']+1] = -1
    return min
    
def keyOf(iheap,  index):
    validateIndex(iheap, i)
    if(not contains(iheap, index)):
        raise Exception('index is not in the priority queue')
    else:
        return iheap['keys'][index]

def changeKey(iheap, i, key):
    validateIndex(iheap, i)
    if(not contains(iheap, i)):
        raise Exception('index is not in the priority queue')

    iheap['keys'][i] = key
    swim(iheap, iheap['qp'][i])
    sink(iheap, iheap['qp'][i])



def decreaseKey(iheap, i,  key):
    validateIndex(iheap, i)
    if not contains(iheap, i):
        raise Exception('index is not in the priority queue')
    if iheap['compare'](iheap['keys'][i], key) < 0:
        raise Exception('Calling decreaseKey() with a key strictly greater than the key in the priority queue')
    iheap['keys'][i] = key
    swim(iheap, iheap['qp'][i])

def increaseKey(iheap, i,  key):
    validateIndex(iheap, i)
    if not contains(iheap, i):
        raise Exception('index is not in the priority queue')
    if iheap['compare'](iheap['keys'][i], key) > 0:
        raise Exception('Calling increaseKey() with a key strictly less than the key in the priority queue')
    iheap['keys'][i] = key
    sink(iheap, iheap['qp'][i])


def delete(iheap, i):
    validateIndex(iheap, i)
    if (not contains(iheap, i)):
        raise Exception("index is not in the priority queue")
    index = iheap['qp'][i]
    exch(iheap, index, iheap['n'])
    iheap['n'] = iheap['n'] - 1
    swim(iheap, index)
    sink(iheap, index)
    keys[i] = None
    iheap['qp'][i] = -1
    

def validateIndex(iheap, i):
    if (i < 0):
        raise Exception("index is negative: " + i)
    if (i >= iheap['maxN']):
        raise Exception("index >= capacity: " + i)

def greater(iheap, i, j):
    return iheap['compare'](iheap['keys'][iheap['pq'][i]], (iheap['keys'][iheap['pq'][j]])) > 0

def exch(iheap, i, j):
    swap = iheap['pq'][i]
    iheap['pq'][i] = iheap['pq'][j]
    iheap['pq'][j] = swap
    iheap['qp'][iheap['pq'][i]] = i
    iheap['qp'][iheap['pq'][j]] = j


def swim(iheap, k):
    while (k > 1 and greater(iheap, k//2, k)):
        exch(iheap, k, k//2)
        k = k//2

def sink(iheap, k):
    while (2*k <= iheap['n']):
        j = 2*k
        if (j < iheap['n'] and greater(iheap, j, j+1)):
            j = j + 1
        if (not greater(iheap, k, j)):
            break
        exch(iheap, k, j)
        k = j
