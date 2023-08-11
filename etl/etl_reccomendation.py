import pandas as pd

# Cargar el DataFrame original desde 'movies_dataset.csv'
df_movies = pd.read_csv('movies_dataset.csv')
print('df_movies', df_movies)

# Filtrar las filas donde 'belongs_to_collection' no es vacío
df_test = df_movies[df_movies['belongs_to_collection'].notnull()].copy()
print('df_test', df_test)

# Filtrar filas donde 'title' y 'overview' no son nulos ni vacíos
df_test = df_test[(df_test['title'].notnull() & df_test['title'].astype(str).str.strip() != '') &
                  (df_test['overview'].notnull() & df_test['overview'].astype(str).str.strip() != '')].copy()

print('df_test 2', df_test)

# Conservar solo las columnas 'title' y 'overview'
df_test = df_test[['title', 'overview']].copy()
df_title = df_movies[['title']].copy()

# Guardar df_test en formato parquet
df_test.to_parquet('pq_reccomCol.parquet', index=False)
df_title.to_parquet('pq_reccomTit.parquet', index=False)
print(df_test.columns)
print(df_title.columns)

# Filtrar las filas donde 'vote_count' es mayor y 'belongs_to_collection' no tiene valores válidos
df_votes = df_movies[(df_movies['vote_count'].notnull()) & (df_movies['belongs_to_collection'].isnull())]
df_votes = df_votes.nlargest(4000, 'vote_count').copy()

# Conservar solo las columnas 'title' y 'overview'
df_votes = df_votes[['title', 'overview']].copy()

# Concatenar df_test y df_votes en un solo DataFrame df_reccom10
df_reccom4 = pd.concat([df_test, df_votes], ignore_index=True)

# Mostrar la cantidad de registros en df_reccom10
num_records_df_reccom4 = len(df_reccom4)
print(f"Cantidad de registros en df_reccom4: {num_records_df_reccom4}")

df_reccom4.to_parquet('pq_reccom4.parquet', index=False)