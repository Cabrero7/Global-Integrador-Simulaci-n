
from sympy import isprime, gcd, divisors
import matplotlib.pyplot as plt
from chi_cuadrada import validar_chi_cuadrada
from distribucion_empirica import calcular_distribuciones
from validaciones_extras import calcular_entropia
import os
import random

def generador_mixto(a, b, m, semilla, cantidad):
    numeros = []
    x = semilla
    for _ in range(cantidad):
        x = (a * x + b) % m
        numeros.append(x / m)
    return numeros

def generador_multiplicativo(a, m, semilla, cantidad):
    numeros = []
    x = semilla
    for _ in range(cantidad):
        x = (a * x) % m
        numeros.append(x / m)
    return numeros

def generador_bits_sistema(cantidad):
    return [int.from_bytes(os.urandom(4), "big") / 2**32 for _ in range(cantidad)]

def evaluar_ciclo_completo_mixto(a, b, m):
    razones = []
    condicion1 = gcd(m, b) == 1
    razones.append("1) m y b son primos entre sí: " + ("✅" if condicion1 else "❌"))
    primos_que_dividen_m = [d for d in divisors(m) if isprime(d)]
    condicion2 = all((a - 1) % q == 0 for q in primos_que_dividen_m)
    razones.append("2) Todo primo q que divide a m también divide a (a - 1): " + ("✅" if condicion2 else "❌"))
    condicion3 = (m % 4 != 0) or ((a - 1) % 4 == 0)
    razones.append("3) Si 4 divide a m, entonces 4 divide a (a - 1): " + ("✅" if condicion3 else "❌"))
    es_ciclo_completo = condicion1 and condicion2 and condicion3
    return es_ciclo_completo, razones

def explicar_raiz_primitiva(a, m):
    explicaciones = []
    if a == 0:
        explicaciones.append("a = 0, por lo tanto NO es raíz primitiva.")
        return False, explicaciones
    factores_primos = [d for d in divisors(m-1) if isprime(d)]
    es_raiz_primitiva = True
    for p in factores_primos:
        exponente = (m-1)//p
        resultado = pow(a, exponente, m)
        if resultado == 1:
            explicaciones.append(f"Para p={p}: a^(({m-1})/{p}) mod {m} = {a}^{exponente} mod {m} = 1 ❌")
            es_raiz_primitiva = False
        else:
            explicaciones.append(f"Para p={p}: a^(({m-1})/{p}) mod {m} = {a}^{exponente} mod {m} = {resultado} ✅")
    if es_raiz_primitiva:
        explicaciones.insert(0, "a es raíz primitiva de m, el ciclo es máximo (t = m-1).")
    else:
        explicaciones.insert(0, "a NO es raíz primitiva de m, el ciclo NO es máximo.")
    return es_raiz_primitiva, explicaciones

def obtener_longitud_periodo(a, b, m, semilla, es_mixto=True):
    vistos = {}
    x = semilla
    i = 0
    while True:
        x = (a * x + b) % m if es_mixto else (a * x) % m
        if x in vistos:
            return i - vistos[x]
        vistos[x] = i
        i += 1

if __name__ == "__main__":
    print("Seleccione el tipo de generador:")
    print("1 - Congruencial Lineal Mixto")
    print("2 - Congruencial Lineal Multiplicativo")
    print("3 - Generador basado en bits del sistema")
    opcion = input("Ingrese 1, 2 o 3: ")

    if opcion == "1":
        a = int(input("Ingrese el valor de a (multiplicador): "))
        b = int(input("Ingrese el valor de b (incremento): "))
        m = int(input("Ingrese el valor de m (módulo): "))
        semilla = int(input("Ingrese la semilla: "))
        cantidad = int(input("¿Cuántos números desea generar?: "))
        numeros = generador_mixto(a, b, m, semilla, cantidad)
        periodo = obtener_longitud_periodo(a, b, m, semilla, es_mixto=True)
        ciclo_completo, explicaciones = evaluar_ciclo_completo_mixto(a, b, m)
        print("\nNúmeros generados:")
        print(numeros)
        print(f"\n🔁 Longitud del período: {periodo}")
        print(f"✅ ¿Es ciclo completo?: {'Sí' if ciclo_completo else 'No'}")
        print("\n📘 Explicación:")
        for razon in explicaciones:
            print("-", razon)

    elif opcion == "2":
        a = int(input("Ingrese el valor de a (multiplicador): "))
        m = int(input("Ingrese el valor de m (módulo): "))
        semilla = int(input("Ingrese la semilla: "))
        cantidad = int(input("¿Cuántos números desea generar?: "))
        numeros = generador_multiplicativo(a, m, semilla, cantidad)
        periodo = obtener_longitud_periodo(a, 0, m, semilla, es_mixto=False)
        es_maximo, explicaciones = explicar_raiz_primitiva(a, m)
        print("\nNúmeros generados:")
        print(numeros)
        print(f"\n🔁 Longitud del período: {periodo}")
        print(f"📏 ¿Tiene longitud máxima (m-1 = {m-1})?: {'Sí' if periodo == m-1 else 'No'}")
        print("\n📘 Explicación:")
        for razon in explicaciones:
            print("-", razon)

    elif opcion == "3":
        cantidad = int(input("¿Cuántos números desea generar?: "))
        numeros = generador_bits_sistema(cantidad)
        print("\nNúmeros generados:")
        print(numeros)

    else:
        print("Opción inválida. Por favor ingrese 1, 2 o 3.")
        exit()

    print("\n--- Validación Chi-cuadrada ---")
    while True:
        intervalos = int(input("¿En cuántos intervalos dividir el rango [0,1)? (2 o 5): "))
        if intervalos in [2, 5]:
            break
        print("Solo se permite 2 o 5 intervalos.")

    alpha = float(input("Ingrese el nivel de significancia (ej: 0.05): "))
    resultado = validar_chi_cuadrada(numeros, intervalos, alpha)

    print("\n--- Validación Chi-cuadrada ---")
    print("FO (frecuencias observadas):", resultado["FO"])
    print("FE (frecuencia esperada):", resultado["FE"])
    print(f"Chi2 calculado: {resultado['chi2_stat']:.4f}")
    print(f"Valor crítico (gl={resultado['gl']}, alpha={alpha}): {resultado['valor_critico']:.4f}")
    print("¿Cumple la prueba?:", "Sí" if resultado["cumple"] else "No")

    print("\n--- Validación por Entropía ---")
    entropia = calcular_entropia(numeros)
    print(f"Entropía Shannon: {entropia:.4f} bits")

    print("\n--- Distribución empírica ---")
    paso = 1 / intervalos
    intervalos_lista = [(round(i * paso, 4), round((i + 1) * paso, 4)) for i in range(intervalos)]
    frecuencias = list(resultado["FO"])
    tabla = calcular_distribuciones(frecuencias, intervalos_lista)

    print("Intervalo      | Frecuencia | Probabilidad | Acumulada")
    print("-" * 52)
    for intv, f, p, a in zip(tabla["intervalos"], tabla["frecuencias"], tabla["probabilidades"], tabla["acumulada"]):
        print(f"{str(intv):<13} | {f:^10} | {p:^12.2f} | {a:^9.2f}")

    etiquetas = [f"{a}-{b}" for a, b in tabla["intervalos"]]
    probabilidades = tabla["probabilidades"]
    acumulada = tabla["acumulada"]

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.bar(etiquetas, probabilidades, color='skyblue')
    for i, v in enumerate(probabilidades):
        plt.text(i, v + 0.01, f"{v:.2f}", ha='center')
    plt.title("Distribución de PROBABILIDAD")
    plt.ylim(0, max(probabilidades) + 0.1)
    plt.xlabel("Intervalo")
    plt.ylabel("Probabilidad")
    plt.xticks(rotation=45, ha='right', fontsize=8)

    plt.subplot(1, 2, 2)
    plt.plot(etiquetas, acumulada, marker='o', color='orange')
    for i, v in enumerate(acumulada):
        plt.text(i, v + 0.02, f"{v:.2f}", ha='center')
    plt.title("Distribución ACUMULATIVA")
    plt.ylim(0, 1.1)
    plt.xlabel("Intervalo")
    plt.ylabel("Acumulada")
    plt.xticks(rotation=45, ha='right', fontsize=8)

    plt.tight_layout()
    plt.show()
