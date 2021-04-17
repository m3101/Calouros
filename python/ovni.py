import math
a, b = map(int, input().split())
numeros = range(a,b+1)
#Encontramos os quadrados
indices_quadrados = [i for i in numeros if math.sqrt(i).is_integer()]
ovnis = len(indices_quadrados)
if ovnis < 2:
  print(0)
else:
  intervalos = [indices_quadrados[i+1]-indices_quadrados[i] for i in range(len(indices_quadrados)-1)]
  print(max(intervalos))
