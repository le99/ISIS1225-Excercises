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

animales = map.newMap(12007, maptype='PROBING', comparefunction=comp)

#                id,
map.put(animales, "1", {"tipo": "ave", "num_pies": 2, "nombre": "colibri"})
map.put(animales, "2", {"tipo": "insecto", "num_pies": 6, "nombre": "mariposa"})
map.put(animales, "3", {"tipo": "mamifero", "num_pies": 4, "nombre": "perro"})
map.put(animales, "4", {"tipo": "mamifero", "num_pies": 0, "nombre": "ballena"})
map.put(animales, "5", {"tipo": "ave", "num_pies": 2, "nombre": "avestrus"})

#========================================
# Quiero buscar los animales por tipo y num_pies
#========================================

animalesPorTipoYNumPies = map.newMap(12007, maptype='PROBING', comparefunction=comp)


keys = map.keySet(animales)
i = listiterator.newIterator(keys)
while listiterator.hasNext(i):
    k = listiterator.next(i)
    v = map.get(animales, k)["value"]

    if map.get(animalesPorTipoYNumPies, v["tipo"] + "$" + str(v["num_pies"])) == None:
        t = lst.newList('LINKED_LIST')
        lst.addLast(t, v)
        map.put(animalesPorTipoYNumPies, v["tipo"] + "$" + str(v["num_pies"]), t)
    else:
        lst.addLast(
            map.get(animalesPorTipoYNumPies, v["tipo"] + "$" + str(v["num_pies"]))["value"],
            v)


keys = map.keySet(animalesPorTipoYNumPies)
i = listiterator.newIterator(keys)
while listiterator.hasNext(i):
    k = listiterator.next(i)
    v = map.get(animalesPorTipoYNumPies, k)["value"]

    tipo = k.split("$")[0]
    num_pies = k.split("$")[1]
    print(tipo, num_pies)

    i2 = listiterator.newIterator(v)
    while listiterator.hasNext(i2):
        k2 = listiterator.next(i2)
        print("\t",k2)