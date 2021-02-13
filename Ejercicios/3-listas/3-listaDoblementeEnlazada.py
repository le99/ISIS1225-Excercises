#Nodo de una lista senciallamente encadenada

# nodo = {
#   'info': None,
#   'next': None  #Puede apuntar al siguiente elemento
#   'prev': None
# }

global first
global last
global size

first = {
  'info': 'a',
  'next': None,
  'prev': None
}


first['next'] = {
  'info': 'b',
  'next': None,
  'prev': first
}


first['next']['next'] = {
  'info': 'c',
  'next': None,
  'prev': first['next']
}

last = first['next']['next']

print('Tercero:', last['info'])
print('Segundo:', last['prev']['info'])
print('Primero:', first['info'])
