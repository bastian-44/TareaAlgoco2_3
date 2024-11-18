//
// Created by Basti on 12-11-2024.
//
#include "cost_functions.h"

const string alphabet = "abcdefghijklmnopqrstuvwxyz";
map<char, int> dict;
bool dict_initialized = false;

vector<vector<int>> cost_replace_matrix(26, vector<int>(26, 0));
vector<int> cost_insert_vector(26, 0);
vector<int> cost_delete_vector(26, 0);
vector<vector<int>> cost_transpose_matrix(26, vector<int>(26, 0));

bool cost_matrices_loaded = false;

void initialize_dict() {
    if (!dict_initialized) {
        for (int i = 0; i < 26; ++i) {
            dict[alphabet[i]] = i;
        }
        dict_initialized = true;
    }
}

void load_cost_matrices() {
    if (cost_matrices_loaded) return;

    ifstream file;

    file.open("./Matrices/cost_replace.txt");
    if (file.is_open()) {
        for (int i = 0; i < 26; ++i) {
            for (int j = 0; j < 26; ++j) {
                file >> cost_replace_matrix[i][j];
            }
        }
        file.close();
    } else {
        cerr << "No se pudo abrir cost_replace.txt" << endl;
    }

    file.open("./Matrices/cost_insert.txt");
    if (file.is_open()) {
        for (int i = 0; i < 26; ++i) {
            file >> cost_insert_vector[i];
        }
        file.close();
    } else {
        cerr << "No se pudo abrir cost_insert.txt" << endl;
    }

    file.open("./Matrices/cost_delete.txt");
    if (file.is_open()) {
        for (int i = 0; i < 26; ++i) {
            file >> cost_delete_vector[i];
        }
        file.close();
    } else {
        cerr << "No se pudo abrir cost_delete.txt" << endl;
    }

    file.open("./Matrices/cost_transpose.txt");
    if (file.is_open()) {
        for (int i = 0; i < 26; ++i) {
            for (int j = 0; j < 26; ++j) {
                file >> cost_transpose_matrix[i][j];
            }
        }
        file.close();
    } else {
        cerr << "No se pudo abrir cost_transpose.txt" << endl;
    }

    cost_matrices_loaded = true;
}

int costo_sub(char a, char b) {
    initialize_dict();
    load_cost_matrices();
    return cost_replace_matrix[dict[a]][dict[b]];
}

int costo_ins(char a) {
    initialize_dict();
    load_cost_matrices();
    return cost_insert_vector[dict[a]];
}

int costo_del(char a) {
    initialize_dict();
    load_cost_matrices();
    return cost_delete_vector[dict[a]];
}

int costo_trans(char a, char b) {
    initialize_dict();
    load_cost_matrices();
    return cost_transpose_matrix[dict[a]][dict[b]];
}
