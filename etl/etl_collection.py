import pandas as pd

# Cargar el archivo 'movies_dataset.csv' en un DataFrame
df_movies = pd.read_csv('movies_dataset.csv')


# Crear la columna 'collection' y completar con los valores 'name' de la columna 'belongs_to_collection'
def get_collection_name(x):
    if pd.notnull(x):
        try:
            collection_data = eval(x)
            if isinstance(collection_data, dict) and 'name' in collection_data:
                return collection_data['name']
        except (SyntaxError, NameError, TypeError):
            pass
    return None


df_movies['collection'] = df_movies['belongs_to_collection'].apply(get_collection_name)

# Rellenar los valores nulos en las columnas 'revenue' y 'budget' con 0
df_movies['revenue'] = df_movies['revenue'].fillna(0)
df_movies['budget'] = df_movies['budget'].fillna(0)

# Convertir los valores de 'revenue' y 'budget' a valores numéricos
df_movies['revenue'] = pd.to_numeric(df_movies['revenue'], errors='coerce')
df_movies['budget'] = pd.to_numeric(df_movies['budget'], errors='coerce')

# Crear la columna 'return' con 'revenue' dividido por 'budget' (0 cuando 'budget' es 0)
df_movies['return'] = df_movies.apply(lambda row: row['revenue'] / row['budget'] if row['budget'] != 0 else 0, axis=1)

# Crear un nuevo DataFrame df_collections con las columnas requeridas
df_collections = df_movies[['collection', 'title', 'revenue']].copy()

# Eliminar las filas que tienen valores faltantes en la columna 'collection'
df_collections = df_collections.dropna(subset=['collection'])

df_collections.to_parquet('pq_collections.parquet', index= False)

print(df_collections.head(10))
