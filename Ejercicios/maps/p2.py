import config as conf
from DISClib.ADT import map as map
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator
from DISClib.ADT import list as lst

#Crear map/dictionary

def comp(key, element):
    if (key == me.getKey(element)):
        return 0
    elif key > me.getKey(element):
        return 1
    else:
        return -1  

comidas = map.newMap(12007, maptype='PROBING', comparefunction=comp)

#                comida,    tipo
map.put(comidas, "manzana", "fruta")
map.put(comidas, "banano", "fruta")
map.put(comidas, "lechuga", "verdura")
map.put(comidas, "espinaca", "verdura")
map.put(comidas, "almendra", "nuez")

#========================================
# Quiero saber cuales son las comidas de cada tipo
#========================================

tiposDeComida = map.newMap(12007, maptype='PROBING', comparefunction=comp)

keys = map.keySet(comidas)
i = listiterator.newIterator(keys)
while listiterator.hasNext(i):
    k = listiterator.next(i)
    v = map.get(comidas, k)["value"]

    if map.get(tiposDeComida, v) == None:
        t = lst.newList('LINKED_LIST')
        lst.addLast(t, k)
        map.put(tiposDeComida, v, t)
    else:
        lst.addLast(
            map.get(tiposDeComida, v)["value"],
            k)


keys = map.keySet(tiposDeComida)
i = listiterator.newIterator(keys)
while listiterator.hasNext(i):
    k = listiterator.next(i)
    v = map.get(tiposDeComida, k)["value"]
    print(k)
    
    i2 = listiterator.newIterator(v)
    while listiterator.hasNext(i2):
        k = listiterator.next(i2)
        print("\t",k)
