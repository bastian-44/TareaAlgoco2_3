
# import pandas with shortcut 'pd'
import pandas as pd

# read_csv function which is used to read the required CSV file
data = pd.read_csv('datasets_resultados_DP.csv')

# display
print("Original 'input.csv' CSV Data: \n")
print(data)

# drop function which is used in removing or deleting rows or columns from the CSV files
data.drop('cadena1', inplace=True, axis=1)
data.drop('cadena2', inplace=True, axis=1)
# display
print("\nCSV Data after deleting the column 'year':\n")
print(data)