// Created by bastian on 25/10/2024.

#ifndef COST_FUNCTIONS_H
#define COST_FUNCTIONS_H

#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

extern const string alphabet;
extern map<char, int> dict;
extern bool dict_initialized;

extern vector<vector<int>> cost_replace_matrix;
extern vector<int> cost_insert_vector;
extern vector<int> cost_delete_vector;
extern vector<vector<int>> cost_transpose_matrix;

extern bool cost_matrices_loaded;

void initialize_dict();
void load_cost_matrices();

int costo_sub(char a, char b);
int costo_ins(char a);
int costo_del(char a);
int costo_trans(char a, char b);

#endif // COST_FUNCTIONS_H
