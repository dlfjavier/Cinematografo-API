import pandas as pd

def peliculas_idioma0(Idioma: str):
    # Cargar el DataFrame desde el archivo 'pq_prodCo.parquet'
    df_languages = pd.read_parquet('datasets/pq_languages.parquet')

    # Contador para almacenar la cantidad de películas en el idioma dado
    cantidad_peliculas = 0

    # Recorrer cada fila del DataFrame y contar las películas en el idioma dado
    for idiomas in df_languages['Languages']:
        for idioma in idiomas:
            if idioma['name'] == Idioma:
                cantidad_peliculas += 1
                break  # Solo contamos una vez por película

    # Construir el mensaje de retorno con el número de películas y el idioma
    mensaje = f"{cantidad_peliculas} película{'s' if cantidad_peliculas != 1 else ''} fueron estrenadas en idioma {Idioma}"

    return mensaje

'''df_languages = pd.read_parquet('datasets/pq_languages.parquet')
print(df_languages.columns)'''

def peliculas_idioma(Idioma: str):
    # Cargar el DataFrame desde el archivo 'pq_prodCo.parquet'
    df_languages = pd.read_parquet('datasets/pq_languages.parquet')

    # Buscar el idioma en el DataFrame
    idioma_info = df_languages[df_languages['Languages'] == Idioma]

    if len(idioma_info) == 0:
        return "No se encontró información para el idioma especificado."

    cantidad_peliculas = idioma_info['Movies'].iloc[0]

    if cantidad_peliculas == 1:
        return f"Se produjo 1 película en el idioma {Idioma}"
    else:
        return f"Se produjeron {cantidad_peliculas} películas en el idioma {Idioma}"


# Ejemplos de uso de la función peliculas_idioma
print(peliculas_idioma('English'))
print(peliculas_idioma('Français'))
print(peliculas_idioma('Español'))
print(peliculas_idioma('Hausa'))
