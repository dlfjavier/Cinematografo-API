import pandas as pd
import ast

# Cargar el archivo 'movies_dataset.csv' en un DataFrame
df_movies = pd.read_csv('movies_dataset.csv')
print("Cantidad de filas antes del filtrado:", len(df_movies))

# Filtrar las filas que contienen objetos diccionario con la clave 'iso_3166_1' en la columna 'production_countries'
def filter_dict(row):
    try:
        countries_list = ast.literal_eval(row)
        return any(isinstance(country, dict) and 'iso_3166_1' in country for country in countries_list)
    except (ValueError, TypeError):
        return False

df_filtrado = df_movies[df_movies['production_countries'].apply(filter_dict)]

# Mostrar la cantidad de filas después del filtrado
print("Cantidad de filas despues del filtrado:", len(df_filtrado))

# Crear una lista de diccionarios para almacenar los valores únicos de 'countries' y 'countries_keys'
import pandas as pd
import ast

# Cargar el archivo 'movies_dataset.csv' en un DataFrame
df_movies = pd.read_csv('movies_dataset.csv')
print("Cantidad de filas antes del filtrado:", len(df_movies))

# Filtrar las filas que contienen objetos diccionario con la clave 'iso_3166_1' en la columna 'production_countries'
def filter_dict(row):
    try:
        countries_list = ast.literal_eval(row)
        return any(isinstance(country, dict) and 'iso_3166_1' in country for country in countries_list)
    except (ValueError, TypeError):
        return False

df_filtrado = df_movies[df_movies['production_countries'].apply(filter_dict)]

# Mostrar la cantidad de filas después del filtrado
print("Cantidad de filas despues del filtrado:", len(df_filtrado))

# Crear una lista de diccionarios para almacenar los valores únicos de 'countries' y 'countries_keys'
countries_data = []

# Iterar sobre cada fila del DataFrame filtrado para obtener los valores únicos
for row in df_filtrado['production_countries']:
    countries_list = ast.literal_eval(row)
    for country in countries_list:
        if isinstance(country, dict) and 'iso_3166_1' in country and 'name' in country:
            country_name = country['name']
            country_iso_3166_1 = country['iso_3166_1']
            countries_data.append({'countries': country_name, 'countries_keys': country_iso_3166_1})

# Crear el DataFrame df_countries a partir de la lista de diccionarios
df_countries = pd.DataFrame(countries_data)

# Eliminar valores en 'countries_keys' que no tienen su equivalente en 'countries'
df_countries = df_countries.dropna()

# Mostrar el DataFrame df_countries resultante
print(df_countries)
