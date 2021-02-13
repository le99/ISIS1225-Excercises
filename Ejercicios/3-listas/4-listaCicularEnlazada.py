#Nodo de una lista senciallamente encadenada

# nodo = {
#   'info': None,
#   'next': None  #Puede apuntar al siguiente elemento
# }

global last
global size

last = {
  'info': 'c',
  'next': None
}


last['next'] = {
  'info': 'a',
  'next': None
}


last['next']['next'] = {
  'info': 'b',
  'next': last
}

size = 3

print('Primero:', last['next']['info'])
print('Segundo:', last['next']['next']['info'])
print('Tercero:', last['info'])
