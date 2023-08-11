import pandas as pd
import ast

# Cargar el archivo CSV en un DataFrame movies_metadata
movies_metadata = pd.read_csv('movies_dataset.csv')

# Rellenar los valores NaN en la columna 'spoken_languages' con una lista vacía
movies_metadata['spoken_languages'].fillna("[]", inplace=True)

# Convertir la columna 'spoken_languages' en una lista de diccionarios
movies_metadata['spoken_languages'] = movies_metadata['spoken_languages'].apply(ast.literal_eval)

# Crear un DataFrame auxiliar para almacenar los idiomas únicos y la cantidad de veces que aparecen
idiomas_contador = {}

# Recorrer cada fila del DataFrame y contar los idiomas únicos
for idiomas in movies_metadata['spoken_languages']:
    for idioma in idiomas:
        nombre_idioma = idioma['name']
        if nombre_idioma in idiomas_contador:
            idiomas_contador[nombre_idioma] += 1
        else:
            idiomas_contador[nombre_idioma] = 1

# Crear el DataFrame df_languages a partir del diccionario de idiomas y sus conteos
df_languages = pd.DataFrame(list(idiomas_contador.items()), columns=['Languages', 'Movies'])

# Imprimir el DataFrame df_idiomas
print(df_languages)

# Imprimir la suma de los valores únicos (cantidad de idiomas distintos)
#print("Suma de valores únicos:", len(df_idiomas))

df_languages.to_parquet('pq_languages.parquet', index= False)


