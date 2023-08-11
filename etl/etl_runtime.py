import pandas as pd

df_movies = pd.read_csv('movies_dataset.csv')

#Convertir 'release_date' a formato datetime y manejar valores
df_movies['release_date'] = pd.to_datetime(df_movies['release_date'], errors='coerce')

#Eliminar los valores nulos del campo 'release_date'
df_movies = df_movies.dropna(subset=['release_date'])

#Crear la columna 'year' y completarla con el año
df_movies['year'] = df_movies['release_date'].dt.year

# Convertir 'runtime' a tipo numérico y dividir por 10 para obtener 'runtime_min'
df_movies['runtime_min'] = pd.to_numeric(df_movies['runtime'], errors='coerce')

# Paso 6: Generar un df_runtime con las columnas 'title', 'year' y 'runtime_min'
df_runtime = df_movies[['title', 'year', 'runtime_min']]

df_runtime.to_parquet('pq_runtime.parquet', index= False)

