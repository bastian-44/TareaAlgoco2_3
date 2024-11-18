import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
# Leer el CSV generado
archivo_csv = "datasets_resultados_DP.csv"
#archivo_csv = "datasets_resultados_BF.csv"
df = pd.read_csv(archivo_csv)

# Configurar estilo de gráficos
sns.set(style="whitegrid")

# 1. Tiempo de ejecución vs. Tamaño de cadena
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="tamano", y="tiempo", marker="o", label="Tiempo de ejecución (s)")
plt.title("Tiempo de ejecución vs. Tamaño de cadena")
plt.xlabel("Tamaño de cadena")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.savefig("tiempo_vs_tamano.png")
plt.close()

# 2. Uso de memoria física vs. Tamaño de cadena
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="tamano", y="memoria_fisica_usada_por_proceso_kb", marker="o", label="Memoria física (KB)")
plt.title("Uso de memoria física vs. Tamaño de cadena")
plt.xlabel("Tamaño de cadena")
plt.ylabel("Memoria física usada (KB)")
plt.legend()
plt.savefig("memoria_vs_tamano.png")
plt.close()

# 3. Distancia mínima de edición vs. Tamaño de cadena
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="tamano", y="distancia", marker="o", label="Distancia mínima de edición")
plt.title("Distancia mínima de edición vs. Tamaño de cadena")
plt.xlabel("Tamaño de cadena")
plt.ylabel("Distancia mínima de edición")
plt.legend()
plt.savefig("distancia_vs_tamano.png")
plt.close()

uso_cpu_promedio = df.groupby("tamano")["uso_cpu_total_final"].mean()

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
uso_cpu_promedio.plot(kind="bar", color="skyblue", edgecolor="black")

# Configurar el gráfico
plt.title("Uso Promedio de CPU por Tamaño de Cadena", fontsize=14)
plt.xlabel("Tamaño de Cadena", fontsize=12)
plt.ylabel("Uso de CPU (%)", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Guardar el gráfico
plt.savefig("cpu_vs_tamano_barras.png", dpi=300)
plt.close()

print("Gráficos generados y guardados como imágenes.")
