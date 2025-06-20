
from collections import Counter
import math

def calcular_entropia(numeros, bins=10):
    etiquetas = [int(n * bins) for n in numeros]
    conteo = Counter(etiquetas)
    total = sum(conteo.values())
    probabilidades = [f / total for f in conteo.values()]
    entropia = -sum(p * math.log2(p) for p in probabilidades if p > 0)
    return entropia
