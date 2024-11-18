import random
import string
import subprocess
import json
import pandas as pd
import time

def generar_cadena(tamano, repetida=False, seed=None, repeticiones=0):
    """Genera una cadena aleatoria o con caracteres repetidos."""
    if seed is not None:
        random.seed(seed + repeticiones)  # Establece la semilla para replicabilidad

    if repetida:
        caracter = random.choice(string.ascii_lowercase)
        return caracter * tamano
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(tamano))


def ejecutar_algoritmo(algoritmo, cadena1, cadena2, modo):
    """
    Ejecuta un algoritmo C++ para calcular la distancia de edición.
    """
    try:
        # Ejecuta el programa con las cadenas y el modo especificado
        resultado = subprocess.run(
            [algoritmo, cadena1, cadena2, modo],
            capture_output=True,
            text=True
        )
        # Parsear la salida como JSON
        salida = json.loads(resultado.stdout.strip())
        return salida
    except Exception as e:
        print(f"Error ejecutando el algoritmo: {e}")
        return None


def generar_datasets(tamanos, repeticiones, algoritmo, modos, seed=None):
    """
    Genera datasets para diferentes tamaños de cadenas y ejecuta los algoritmos.
    """
    datos = []
    for tamano in tamanos:
        for repeticion in range(repeticiones):
            for modo in modos:
                # Cadenas aleatorias
                cadena1 = generar_cadena(tamano, seed=seed, repeticiones=repeticion)
                cadena2 = generar_cadena(tamano, seed=seed + 50, repeticiones=repeticion)
                resultado = ejecutar_algoritmo(algoritmo, cadena1, cadena2, modo)
                if resultado:
                    datos.append({
                        "tamano": tamano,
                        "repeticion": repeticion,
                        "modo": modo,
                        **resultado  # Agrega todos los datos del JSON generado por el C++
                    })
                print("repeticion ", repeticion, ", de tamaño ", tamano, "lista")

                """cadena1 = generar_cadena(tamano, repetida=True, seed=seed, repeticiones=repeticion)
                cadena2 = generar_cadena(tamano, repetida=True, seed=seed + 50, repeticiones=repeticion)
                resultado = ejecutar_algoritmo(algoritmo, cadena1, cadena2, modo)
                if resultado:
                    datos.append({
                        "tamano": tamano,
                        "repeticion": repeticion,
                        "modo": modo,
                        **resultado  # Agrega todos los datos del JSON generado por el C++
                    }) """
    return datos


def guardar_datasets(datos, archivo_salida):
    """Guarda los datos generados en un archivo CSV."""
    df = pd.DataFrame(datos)
    df.to_csv(archivo_salida, index=False)
    print(f"Datos guardados en {archivo_salida}")


# Configuración
tamanos = [10, 100, 500, 1000, 2000, 2500 ]  # Tamaños de cadenas
repeticiones = 5  # Número de pruebas por tamaño
#modos = ["fuerza_bruta", "dinamica"]  # Algoritmos
modos = ["dinamica"]  # Algoritmos
#modos = ["fuerza_bruta"]  # Algoritmos

algoritmo = "./cmake-build-debug/TareaAlgoco2_3.exe"  # Ruta al ejecutable
archivo_salida = "datasets_resultados_DP.csv"
#archivo_salida = "datasets_resultados_BF.csv"
seed = 42  # Semilla para generar datos replicables

# Medir el tiempo total de ejecución
start_time_total = time.time()

# Generación y guardado de datasets
datos_generados = generar_datasets(tamanos, repeticiones, algoritmo, modos, seed=seed)
guardar_datasets(datos_generados, archivo_salida)

end_time_total = time.time()
total_elapsed_time = end_time_total - start_time_total
print(f"Tiempo total de ejecución: {total_elapsed_time:.2f} segundos")