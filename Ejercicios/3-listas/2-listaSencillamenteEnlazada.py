#Nodo de una lista senciallamente encadenada

# nodo = {
#   'info': None,
#   'next': None  #Puede apuntar al siguiente elemento
# }

global first
global last
global size

first = {
  'info': 'a',
  'next': None
}


first['next'] = {
  'info': 'b',
  'next': None
}


first['next']['next'] = {
  'info': 'c',
  'next': None
}

last = first['next']['next']
size = 3

print('Primero:', first['info'])
print('Segundo:', first['next']['info'])
print('Tercero:', last['info'])
