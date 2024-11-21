import random
import string
import subprocess
import json
import pandas as pd
import time

def generar_cadena(tamano, patron="aleatoria", seed=None, repeticiones=0):
    """
    Genera cadenas según diferentes patrones:

    Parámetros:
    - tamano (int): Longitud de la cadena a generar.
    - patron (str): Patrón para la generación de la cadena. Valores posibles:
        - "aleatoria" (default): Cadena completamente aleatoria.
        - "repetida": Cadena formada por un solo carácter repetido.
        - "mitad_fija": Mitad de la cadena es un carácter fijo, la otra mitad es aleatoria.
        - "transpuesta": Una cadena base con dos caracteres intercambiados.
    - seed (int, opcional): Semilla para la generación de valores aleatorios, asegura reproducibilidad.
    - repeticiones (int, opcional): Número de la repetición actual, usado junto con la semilla.

    Retorno:
    - str: Cadena generada según el patrón especificado.
    """
    if seed is not None:
        random.seed(seed + repeticiones)

    if patron == "repetida":
        caracter = random.choice(string.ascii_lowercase)
        return caracter * tamano

    elif patron == "mitad_fija":
        caracter = random.choice(string.ascii_lowercase)
        mitad_fija = caracter * (tamano // 2)
        mitad_aleatoria = ''.join(random.choice(string.ascii_lowercase) for _ in range(tamano - len(mitad_fija)))
        return mitad_fija + mitad_aleatoria

    elif patron == "transpuesta":
        if tamano < 2:
            return ''.join(random.choice(string.ascii_lowercase) for _ in range(tamano))
        cadena = ''.join(random.choice(string.ascii_lowercase) for _ in range(tamano))
        i, j = random.sample(range(tamano), 2)
        lista_cadena = list(cadena)
        lista_cadena[i], lista_cadena[j] = lista_cadena[j], lista_cadena[i]
        return ''.join(lista_cadena)

    # Default: aleatoria
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(tamano))


def ejecutar_algoritmo(algoritmo, cadena1, cadena2, modo):
    """
    Ejecuta un algoritmo C++ para calcular la distancia de edición entre dos cadenas.

    Parámetros:
    - algoritmo (str): Ruta al ejecutable del algoritmo.
    - cadena1 (str): Primera cadena de entrada.
    - cadena2 (str): Segunda cadena de entrada.
    - modo (str): Metodo de cálculo (por ejemplo, "fuerza_bruta" o "dinamica").

    Retorno:
    - dict: Resultado en formato JSON, parseado desde la salida del programa.
    - None: Si ocurre un error durante la ejecución.
    """
    try:
        resultado = subprocess.run(
            [algoritmo, cadena1, cadena2, modo],
            capture_output=True,
            text=True
        )
        salida = json.loads(resultado.stdout.strip())

        return salida
    except Exception as e:
        print(f"Error ejecutando el algoritmo: {e}")
        return None


def generar_datasets(tamanos, repeticiones, algoritmo, modos, patrones, seed=None):
    """
    Genera un conjunto de datos ejecutando el algoritmo para diferentes tamaños de cadenas, patrones y configuraciones.

    Parámetros:
    - tamanos (list[int]): Lista de tamaños de cadenas a generar.
    - repeticiones (int): Número de pruebas a realizar para cada tamaño.
    - algoritmo (str): Ruta al ejecutable del algoritmo.
    - modos (list[str]): Modos de ejecución del algoritmo (por ejemplo, "fuerza_bruta", "dinamica").
    - patrones (list[str]): Patrones para generar las cadenas (ver `generar_cadena`).
    - seed (int, opcional): Semilla para reproducibilidad.

    Retorno:
    - list[dict]: Lista de resultados con datos para cada combinación de parámetros.
    """
    datos = []
    for tamano in tamanos:
        for repeticion in range(repeticiones):
            for modo in modos:
                for patron in patrones:
                    cadena1 = generar_cadena(tamano, patron=patron, seed=seed, repeticiones=repeticion)
                    cadena2 = generar_cadena(tamano, patron=patron, seed=seed + 50, repeticiones=repeticion)
                    resultado = ejecutar_algoritmo(algoritmo, cadena1, cadena2, modo)
                    if resultado:
                        datos.append({
                            "tamano": tamano,
                            "repeticion": repeticion,
                            "modo": modo,
                            "patron": patron,
                            **resultado
                        })
                    print(f"Repetición {repeticion}, tamaño {tamano}, patrón {patron} lista")
    return datos


def guardar_datasets(datos, archivo_salida):
    """
    Guarda los datos generados en un archivo CSV.

    Parámetros:
    - datos (list[dict]): Lista de resultados generados por `generar_datasets`.
    - archivo_salida (str): Nombre del archivo CSV donde se guardarán los datos.
    """
    df = pd.DataFrame(datos)
    df.to_csv(archivo_salida, index=False)
    print(f"Datos guardados en {archivo_salida}")


# Configuración
tamanos = [6, 7, 8, 9, 10, 11, 12]  # Tamaños de cadenas
repeticiones = 5  # Número de pruebas por tamaño
modos = ["fuerza_bruta"]  # Algoritmos
#modos = ["dinamica"]
patrones = ["aleatoria", "repetida", "mitad_fija", "transpuesta"]  # Patrones de cadenas

algoritmo = "./cmake-build-debug/TareaAlgoco2_3.exe"  # Ruta al ejecutable .exe
archivo_salida = "datasets_resultados_BF.csv"
seed = 42  # Semilla para generar datos replicables

# Medir el tiempo total de ejecución
start_time_total = time.time()

# Generación y guardado de datasets
datos_generados = generar_datasets(tamanos, repeticiones, algoritmo, modos, patrones, seed=seed)
guardar_datasets(datos_generados, archivo_salida)

end_time_total = time.time()
total_elapsed_time = end_time_total - start_time_total
print(f"Tiempo total de ejecución: {total_elapsed_time:.2f} segundos")
