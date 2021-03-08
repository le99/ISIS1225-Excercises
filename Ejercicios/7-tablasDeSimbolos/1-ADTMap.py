import config as cf
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt

#crear

def cmpFunction(key, element):
    key2 = str(element['key'])
    if (key == key2):
        return 0
    elif (key > key2):
        return 1
    else:
        return -1

tablaDeSimbolos = mp.newMap(numelements=2,
                            maptype='PROBING',
                            comparefunction=cmpFunction)
#put
mp.put(tablaDeSimbolos, 'llave1', 'valor1')
mp.put(tablaDeSimbolos, 'llave2', 'valor2')
mp.put(tablaDeSimbolos, 'llave3', 'valor3')

#contains
print(mp.contains(tablaDeSimbolos, 'x'))

#get
v = mp.get(tablaDeSimbolos, 'llave1')
print(v['value'])

# #delete
mp.remove(tablaDeSimbolos, 'llave2')


# #Iterar
print()

for key in lt.iterator(mp.keySet(tablaDeSimbolos)):
  print(key, ': ', mp.get(tablaDeSimbolos, key)['value'])
