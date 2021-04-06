import config

from DISClib.ADT import list as lt
from prettyConverter import prettyConverter as cv

lista = lt.newList()
lt.addLast(lista, 'a')
lt.addLast(lista, 'b')

r = cv(lista)
print(r)