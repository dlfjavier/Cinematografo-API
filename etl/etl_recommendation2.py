import pandas as pd

# Leer el archivo CSV
'''df_movies = pd.read_csv('movies_dataset.csv', low_memory=False)

df_reccom  = df_movies[['title','overview']]
df_reccom.to_parquet('pq_reccom.parquet', index = False)

df_reccomRed = pd.read_parquet('pq_reccom.parquet')
df_reccomRed = df_reccomRed.sample(n=10000)
df_reccomRed.to_parquet('pq_reccomRed.parquet', index = False)'''

# Cargar el archivo 'movies_dataset.csv' en el DataFrame df_movies
df_movies = pd.read_csv('movies_dataset.csv', low_memory=False)

# Mostrar la cantidad de registros en df_movies
#print("Cantidad de registros en df_movies:", len(df_movies))

# Filtrar los registros con valores nulos o vacíos en 'belongs_to_collection'
df_reccomendator = df_movies[df_movies['belongs_to_collection'].isnull()]

# Filtrar los registros sin valores nulos o vacíos en 'belongs_to_collection'
df_reccomendator_notnull = df_movies[df_movies['belongs_to_collection'].notnull()]

# Ordenar los registros por 'vote_count' en orden descendente y tomar los 6000 primeros
df_reccomendator = df_reccomendator.sort_values(by='vote_count', ascending=False).head(6000)

# Concatenar los dos DataFrames
df_reccomendator = pd.concat([df_reccomendator, df_reccomendator_notnull])

# Mostrar la cantidad de registros en df_reccomendator
#print("Cantidad de registros en df_reccomendator:", len(df_reccomendator))

df_reccomendator  = df_reccomendator[['title','overview']]
print(df_reccomendator.columns)
print(df_reccomendator.head())
print(df_reccomendator)
df_reccomendator.to_parquet('pq_reccom.parquet', index = False)