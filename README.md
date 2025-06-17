# 🧮 Generador y Validación de Números Aleatorios en Python

## 📌 Título del Proyecto
**Desarrollo de un generador de números aleatorios, test para validar la sucesión y generación de variables aleatorias mediante la implementación en código Python.**

## 🎯 Introducción / Contexto

En múltiples áreas como la simulación de sistemas, el modelado estadístico y la criptografía, es indispensable contar con números aleatorios de buena calidad. La aleatoriedad no solo debe ser aparente, sino también cumplir con propiedades estadísticas formales para garantizar la fiabilidad de los resultados simulados.

Este proyecto busca desarrollar e implementar generadores congruenciales en Python y validar estadísticamente las secuencias generadas, con el fin de emplearlas en simulaciones o generación de variables aleatorias. Además, se ofrece una base extensible para incorporar métodos adicionales.

## 🎯 Objetivos

### Objetivo General
Implementar y validar generadores de números pseudoaleatorios utilizando Python, evaluando su comportamiento estadístico y su aplicabilidad en simulación.

### Objetivos Específicos
- Desarrollar generadores congruenciales mixto y multiplicativo.
- Evaluar si generan ciclos completos o longitudes máximas.
- Aplicar la prueba de **Chi-cuadrado** para verificar la uniformidad.
- Representar visualmente la distribución empírica de los datos generados.
- Establecer una estructura extensible para futuras implementaciones.

## 🔄 Etapas de simulación

1. **Generación de números aleatorios:**  
   Utilizando métodos congruenciales (mixto y multiplicativo) con parámetros ajustables.

2. **Evaluación de ciclos:**  
   Verificación teórica de si los generadores alcanzan ciclo completo o longitud máxima.

3. **Prueba de uniformidad:**  
   Aplicación de test **Chi-cuadrado** con elección de cantidad de intervalos y nivel de significancia.

4. **Construcción de distribuciones empíricas:**  
   Cálculo de frecuencias, probabilidades y acumuladas. Visualización con `matplotlib`.

5. **Visualización y análisis:**  
   Graficación de los resultados para mejor interpretación de la calidad del generador.

## 🛠️ Herramientas utilizadas

- **Lenguaje:** Python 3.11
- **IDE:** Visual Studio Code
- **Librerías:**
  - `sympy`: para condiciones teóricas (primos, mcd, etc.)
  - `numpy` y `scipy`: para el test chi-cuadrado
  - `matplotlib`: para graficar la distribución empírica

- **Estructura de archivos:**
  ```
  generadorNumeros.py              # Módulo principal con interacción por consola
  chi_cuadrada.py                  # Función de validación estadística
  distribucion_empirica.py        # Cálculo de tablas y acumuladas
  ```

## 📈 Resultados, Análisis y Conclusiones

### Indicadores obtenidos
- Validación de la calidad de las secuencias según el test Chi-cuadrado.
- Visualización clara de las frecuencias y su comportamiento probabilístico.
- Detección de periodos y evaluación de condiciones para ciclos completos.

### Escenarios probados
- Diferentes combinaciones de parámetros `a`, `b`, `m`, y `semilla`.
- Comparación entre generadores mixtos y multiplicativos.

### Aprendizajes
- Comprensión profunda de cómo se forman ciclos en los generadores.
- Relación entre la teoría de números y la aleatoriedad computacional.
- Importancia de validar estadísticamente cualquier fuente de aleatoriedad en simulación.

### Recomendaciones
- Incluir más pruebas estadísticas como Kolmogórov-Smirnov.
- Extender el proyecto con generadores basados en métodos más modernos.
- Modularizar para uso como librería en otros proyectos de simulación.

## ✅ Frase final

**Este proyecto demuestra cómo la implementación consciente y validada de generadores aleatorios es una herramienta fundamental para simulaciones confiables y modelos robustos.**
