#include <bits/stdc++.h>
#include <windows.h>
#include <psapi.h>
#include <pdh.h>
#include <nlohmann/json.hpp> // Biblioteca para manejar JSON
#include "BruteForce.h"
#include "DynamicProgramming.h"

using namespace std;
using json = nlohmann::json;

// Variables globales para memoria y CPU
MEMORYSTATUSEX memInfo;
PROCESS_MEMORY_COUNTERS_EX pmc;
static PDH_HQUERY cpuQuery;
static PDH_HCOUNTER cpuTotal;
static bool pdhInitialized = false;

// Inicialización de PDH y CPU por proceso
void init() {
    if (!pdhInitialized) {
        PdhOpenQuery(NULL, NULL, &cpuQuery);
        PdhAddEnglishCounterW(cpuQuery, L"\\Processor(_Total)\\% Processor Time", NULL, &cpuTotal);
        PdhCollectQueryData(cpuQuery);
        pdhInitialized = true;
    }
}

// Obtener el valor actual del uso total de CPU
double getCurrentCPUUsage() {
    PDH_FMT_COUNTERVALUE counterVal;
    PdhCollectQueryData(cpuQuery);
    PdhGetFormattedCounterValue(cpuTotal, PDH_FMT_DOUBLE, NULL, &counterVal);
    return counterVal.doubleValue;
}

// Optimización en el uso de memoria
void consultarMemoria(SIZE_T &virtualMemUsedByMe, SIZE_T &physMemUsedByMe) {
    // Consultar solo cuando sea necesario
    MEMORYSTATUSEX memInfo;
    memInfo.dwLength = sizeof(MEMORYSTATUSEX);
    GlobalMemoryStatusEx(&memInfo);

    // Consultar el uso de memoria de este proceso
    GetProcessMemoryInfo(GetCurrentProcess(), (PROCESS_MEMORY_COUNTERS*)&pmc, sizeof(pmc));
    virtualMemUsedByMe = pmc.PrivateUsage;
    physMemUsedByMe = pmc.WorkingSetSize;
}

// Función principal
int main(int argc, char* argv[]) {
    if (argc != 4) {
        cerr << "Uso incorrecto. Debe proporcionar dos cadenas y el modo (fuerza_bruta o dinamica)." << endl;
        return 1;
    }

    string cadena1 = argv[1];
    string cadena2 = argv[2];
    string modo = argv[3];

    // Inicializar recursos
    init();

    // Capturar la memoria inicial
    SIZE_T virtualMemUsedByMe, physMemUsedByMe;
    consultarMemoria(virtualMemUsedByMe, physMemUsedByMe);

    double initialCPUUsage = getCurrentCPUUsage();

    // Iniciar medición de tiempo
    clock_t start = clock();

    int distancia = -1;
    if (modo == "fuerza_bruta") {
        distancia = distanciaEdicionFuerzaBruta(cadena1, cadena2);
    } else if (modo == "dinamica") {
        distancia = dynamicProgramming(cadena1, cadena2);
    } else {
        cerr << "Modo no válido. Use 'fuerza_bruta' o 'dinamica'." << endl;
        return 1;
    }

    clock_t stop = clock();
    double elapsed = double(stop - start) / CLOCKS_PER_SEC;

    // Consultar la memoria final
    consultarMemoria(virtualMemUsedByMe, physMemUsedByMe);

    double finalCPUUsage = getCurrentCPUUsage();

    // Salida en formato JSON
    json resultado = {
        {"modo", modo},
        {"cadena1", cadena1},
        {"cadena2", cadena2},
        {"distancia", distancia},
        {"tiempo", elapsed},
        {"uso_cpu_total_inicial", initialCPUUsage},
        {"uso_cpu_total_final", finalCPUUsage},
        {"memoria_virtual_usada_por_proceso_kb", virtualMemUsedByMe / 1024},
        {"memoria_fisica_usada_por_proceso_kb", physMemUsedByMe / 1024}
    };

    cout << resultado.dump(4) << endl;
    return 0;
}
