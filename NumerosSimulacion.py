import random

def centroscuad(seed, n):
    resultados = []
    numdigits = len(str(seed))
    for _ in range(n):
        cuadrado = str(seed ** 2).zfill(2 * numdigits)  
        mid = len(cuadrado) // 2
        seed = int(cuadrado[mid - numdigits // 2:mid + numdigits // 2])
        resultados.append(seed)
    return resultados

def medioscuad(seed, n):
    resultados = []
    numdigits = len(str(seed))
    for _ in range(n):
        cuadrado = str(seed ** 2).zfill(2 * numdigits)  
        mid_start = (len(cuadrado) // 4)
        mid_end = (3 * len(cuadrado) // 4)
        seed = int(cuadrado[mid_start:mid_end])
        resultados.append(seed)
    return resultados

semilla = random.randint(1000, 9999)  
n = 100  

numcentroscuad = centroscuad(semilla, n)
nummedioscuad = medioscuad(semilla, n)

print("Números generados por centros al cuadrado:")
print(numcentroscuad)
print("\nNúmeros generados por medios cuadrados:")
print(nummedioscuad)