#include <bits/stdc++.h>
#include "cost_functions.h"
#include "BruteForce.h"
#include <string>
using namespace std;

// Funciones de costo para cada operación

// Función recursiva de fuerza bruta para calcular la distancia de edición
int distanciaEdicionFuerzaBruta(const string& cadena1, const string& cadena2) {
    int n = cadena1.size();
    int m = cadena2.size();

    // Si una de las cadenas está vacía, costo es la suma de inserciones o eliminaciones
    if (n == 0) return m * costo_ins(' ');
    if (m == 0) return n * costo_del(' ');

    // Si el primer carácter es igual, no hay costo
    if (cadena1[0] == cadena2[0])
        return distanciaEdicionFuerzaBruta(cadena1.substr(1), cadena2.substr(1));

    // Calcular el costo de cada operación
    int costoInsercion = costo_ins(cadena2[0]) + distanciaEdicionFuerzaBruta(cadena1, cadena2.substr(1));
    int costoEliminacion = costo_del(cadena1[0]) + distanciaEdicionFuerzaBruta(cadena1.substr(1), cadena2);
    int costoSustitucion = costo_sub(cadena1[0], cadena2[0]) + distanciaEdicionFuerzaBruta(cadena1.substr(1), cadena2.substr(1));

    // Calcular costo de transposición si es posible
    int costoTransposicion = INT_MAX;
    if (n > 1 && m > 1 && cadena1[0] == cadena2[1] && cadena1[1] == cadena2[0]) {
        costoTransposicion = costo_trans(cadena1[0], cadena1[1]) + distanciaEdicionFuerzaBruta(cadena1.substr(2), cadena2.substr(2));
    }

    // Retornar el mínimo costo entre las operaciones
    return min({costoInsercion, costoEliminacion, costoSustitucion, costoTransposicion});
}
