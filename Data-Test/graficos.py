import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración inicial para gráficos
sns.set(style="whitegrid")

# Carga de datos
data = pd.read_csv('datasets_resultados_BF.csv')  # Cambia 'datos.csv' al nombre de tu archivo CSV

# Convertir tiempo y CPU a float por si están en otro formato
data['tiempo'] = pd.to_numeric(data['tiempo'], errors='coerce')
data['uso_cpu_total_final'] = pd.to_numeric(data['uso_cpu_total_final'], errors='coerce')

# Gráfico 1: Relación entre tamaño y tiempo de ejecución
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='tamano', y='tiempo', hue='patron', marker='o')
plt.title('Relación entre Tamaño y Tiempo de Ejecución')
plt.xlabel('Tamaño')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.legend(title='Patrón')
plt.savefig("tiempo_vs_tamano_BF.png")

# Gráfico 2: Uso de memoria física por tamaño
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='tamano', y='memoria_fisica_usada_por_proceso_kb', hue='patron')
plt.title('Memoria Física Usada por Tamaño')
plt.xlabel('Tamaño')
plt.ylabel('Memoria Física (KB)')
plt.legend(title='Patrón')
plt.savefig('memoria_vs_tamano_BF')


# Gráfico 3: Uso de CPU final según el patrón y tamaño
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='patron', y='uso_cpu_total_final', hue='tamano')
plt.title('Uso de CPU Total Final por Patrón y Tamaño')
plt.xlabel('Patrón')
plt.ylabel('Uso de CPU (%)')
plt.legend(title='Tamaño', loc='upper left')
plt.savefig("cpu_vs_tamano_BF.png")

# Gráfico 4: Distancia promedio por patrón
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='patron', y='distancia')
plt.title('Distancia Promedio por Patrón')
plt.xlabel('Patrón')
plt.ylabel('Distancia')
plt.savefig("distancia_promedio_FB.png")


# Gráfico 5: Comparación de memoria física y virtual
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='memoria_fisica_usada_por_proceso_kb', y='memoria_virtual_usada_por_proceso_kb', hue='tamano', style='patron')
plt.title('Comparación de Memoria Física y Virtual Usada')
plt.xlabel('Memoria Física (KB)')
plt.ylabel('Memoria Virtual (KB)')
plt.legend(title='Tamaño')
plt.savefig("fisica_vs_virtua_BF.png")

