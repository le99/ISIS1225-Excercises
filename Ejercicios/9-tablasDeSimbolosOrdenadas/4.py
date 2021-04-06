# Completar la funcion
def minKeyNode(node, cmpFunction):
  pass

def cmpFunction():
  pass

tree = {
  "root": {
    "key": 50,
    "value": 3,
    "size": 3,
    "left": {
      "key": 10,
      "value": 3,
      "size": 3,
      "left": None,
      "right": None
    },
    "right": {
      "key": 90,
      "value": 3,
      "size": 3,
      "left": None,
      "right": None
    }
  }
}

print(minKeyNode(tree['root'], cmpFunction))