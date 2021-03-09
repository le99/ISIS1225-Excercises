import csv 

tamaNoTabla = 7

personas = []
# Datos de https://www.mockaroo.com/
input_file = csv.DictReader(open('./Ejercicios/7-tablasDeSimbolos/MOCK_DATA.csv', encoding='utf-8'))
for p in input_file:
  personas.append(p)

#Proponer una funcion de Transformacion para una tabla de hash donde las llaves son nombre con edad
def funcionDeTransaformacion(k):
  return 1

for p in personas:
  print(funcionDeTransaformacion(p))

