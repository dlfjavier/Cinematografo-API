import numpy as np
import pandas as pd
import ast
import numpy as np

# Cargar el archivo CSV en un DataFrame
df_movies = pd.read_csv('movies_dataset.csv')
#print(df_movies.info())

df_movies['revenue']= df_movies['revenue'].replace(0, np.nan)
df_movies['budget']= pd.to_numeric(df_movies['budget'], errors = 'coerce')
df_movies['budget']= df_movies['budget'].replace(0, np.nan)

df_movies['return']= df_movies['revenue']/df_movies['budget']

# Filtrar el DataFrame original para obtener solo las filas con valor mayor que 0 en la columna "return"
df_prodCo = df_movies[df_movies['return'] > 0]

#Desanida la columna 'production_companies' para obtener elementos individuales
df_prodCo['production_companies'] = df_prodCo['production_companies'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
df_prodCo['production_companies_clean'] = df_prodCo['production_companies'].apply(lambda x: [item['name'] for item in x] if isinstance(x, list) else [])

unique_classes = list(set([item for sublist in df_prodCo['production_companies_clean'].dropna() for item in sublist]))

print(len(unique_classes))