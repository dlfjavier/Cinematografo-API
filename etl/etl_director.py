import pandas as pd
import ast
import numpy as np

# Carga el archivo 'movies_dataset.csv' en un DataFrame
df_movies = pd.read_csv('movies_dataset.csv', low_memory=False)
# Cargar el archivo 'credits.csv' en un DataFrame
df_credits = pd.read_csv('credits.csv', low_memory=False)

df_movies['revenue']= df_movies['revenue'].replace(0, np.nan)
df_movies['budget']= pd.to_numeric(df_movies['budget'], errors = 'coerce')
df_movies['budget']= df_movies['budget'].replace(0, np.nan)

df_movies['return']= df_movies['revenue']/df_movies['budget']
columns_to_drop = ['adult', 'belongs_to_collection', 'genres', 'homepage',
       'imdb_id', 'original_language', 'original_title', 'overview',
       'popularity', 'poster_path', 'production_companies',
       'production_countries', 'runtime',
       'spoken_languages', 'status', 'tagline', 'video',
       'vote_average', 'vote_count']
df_movies = df_movies.drop(columns_to_drop, axis =1)

# Se procesa columna id en movies
def convert_int(x):
    try:
        return int(x)
    except:
        return np.nan

df_movies['id'] = df_movies['id'].apply(convert_int)
#print(df_movies[df_movies['id'].isnull()])
df_movies = df_movies.drop([19730, 29503, 35587])
df_movies['id'] = df_movies['id'].astype('int')

# Convertir la columna 'crew' de una representación en cadena a un diccionario
df_credits['crew'] = df_credits['crew'].apply(ast.literal_eval)

# Definir una función para extraer el nombre del director de la lista 'crew'
def get_director(crew_list):
    for crew_member in crew_list:
        if crew_member['job'] == 'Director':
            return crew_member['name']
    return None

# Crear la columna 'director' y llenarla con el nombre del director
df_credits['director'] = df_credits['crew'].apply(get_director)

columns_to_drop = ['crew', 'cast']
df_credits = df_credits.drop(columns_to_drop, axis =1)

df_mov_dir = df_movies.merge(df_credits, on = 'id')

cantidad_nan_por_columna = df_mov_dir.isna().sum()

print(cantidad_nan_por_columna)


# Mostrar las primeras 10 filas de df_directors
print(df_credits.head(10))
print(df_mov_dir.head(10))
print('column', df_mov_dir.columns)
df_mov_dir.to_parquet('pq_mov_dir.parquet', index= False)

df_mov_dir_Alt = df_mov_dir.loc[df_mov_dir['return'].isna()]
df_mov_dir_Alt.to_parquet('pq_mov_dir_Alt.parquet', index= False)