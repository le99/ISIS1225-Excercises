#crear
tablaDeSimbolos = {}

#put
tablaDeSimbolos['llave1'] = 'valor1'
tablaDeSimbolos['llave2'] = 'valor2'
tablaDeSimbolos['llave3'] = 'valor3'

#contains
print('x' in tablaDeSimbolos)

#get
v = tablaDeSimbolos['llave1']
print(v)

#delete

del tablaDeSimbolos['llave2']

#Iterar
print()

for key in tablaDeSimbolos.keys():
  print(key, ': ', tablaDeSimbolos[key])
