//
// Created by Basti on 12-11-2024.
//
#include <bits/stdc++.h>
#include "cost_functions.h"
#include <string>
#include "DynamicProgramming.h"

using namespace std;



 int dynamicProgramming(const std::string& cadena1, const std::string& cadena2) {
    int size1 = cadena1.size();
    int size2 = cadena2.size();
    vector<vector<int>> dp(size1 + 1, vector<int>(size2 + 1, 0));  // Matriz dinámica para almacenar los costos.

    // Caso base: cuando una de las palabras es de longitud cero
    for (int i = 0; i <= size1; ++i) dp[i][0] = i > 0 ? dp[i - 1][0] + costo_del(cadena1[i - 1]) : 0;
    for (int j = 0; j <= size2; ++j) dp[0][j] = j > 0 ? dp[0][j - 1] + costo_ins(cadena2[j - 1]) : 0;

    // Llenado de la matriz con los costos correspondientes
    for (int i = 1; i <= size1; ++i) {
        for (int j = 1; j <= size2; ++j) {
            int cost_sub = dp[i - 1][j - 1] + costo_sub(cadena1[i - 1], cadena2[j - 1]);
            int cost_ins = dp[i][j - 1] + costo_ins(cadena2[j - 1]);
            int cost_del = dp[i - 1][j] + costo_del(cadena1[i - 1]);
            dp[i][j] = min({ cost_sub, cost_ins, cost_del });

            // Transposición (opcional)
            if (i > 1 && j > 1 && cadena1[i - 1] == cadena2[j - 2] && cadena1[i - 2] == cadena2[j - 1]) {
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + costo_trans(cadena1[i - 1], cadena1[i - 2]));
            }
        }
    }

    return dp[size1][size2];
}

/*
 * Parte de este código ha sido adaptado del repositorio de GitHub de Guilherme Agostinelli:
 * https://github.com/guilhermeagostinelli/levenshtein
 *
 * Licencia: MIT License
 * Copyright (c) 2019 Guilherme Agostinelli
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
