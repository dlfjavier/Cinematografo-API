from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/get_director/{nombre_director}")
def get_director(nombre_director: str):
    df_mov_dir = pd.read_parquet('datasets/pq_mov_dir.parquet')

    # Filtrar el DataFrame para obtener solo las películas dirigidas por el director dado
    director_movies = df_mov_dir[df_mov_dir['director'] == nombre_director]

    if director_movies.empty:
        # Si no hay películas del director en el DataFrame, retornar mensaje apropiado
        return "No se encontraron películas dirigidas por {}".format(nombre_director)

    # Filtrar para considerar solo los registros con valores numéricos en 'revenue' y 'budget'
    valid_movies = director_movies[
        pd.to_numeric(director_movies['revenue'], errors='coerce').notna() &
        pd.to_numeric(director_movies['budget'], errors='coerce').notna()
        ]

    if valid_movies.empty:
        # Si no hay películas con valores numéricos en 'revenue' y 'budget', retornar mensaje apropiado
        return "No se encontraron películas con información de revenue y budget para {}".format(nombre_director)

    # Calcular el total_return como la división entre la suma de 'revenue' y la suma de 'budget'
    #total_return = valid_movies['revenue'].sum() / valid_movies['budget'].sum()#5.33
    total_return = valid_movies['return'].sum() #310.00
    #total_return = valid_movies['return'].sum() / len(valid_movies['return'])#10.33

    # Preparar la lista de detalles de cada película
    detalles_peliculas = []
    for index, row in director_movies.iterrows():
        pelicula = [
            row['title'],
            row['release_date'],
            '{:,.2f}'.format(row['return']),
            '{:,.2f}'.format(row['budget']) if not pd.isnull(row['budget']) else 'Sin información',
            '{:,.2f}'.format(row['revenue']) if not pd.isnull(row['revenue']) else 'Sin información'
        ]
        detalles_peliculas.append(pelicula)

    # Formatear los valores 'nan' como 'Sin información'
    detalles_peliculas_str = []
    for pelicula in detalles_peliculas:
        detalles_peliculas_str.append([val if val != 'nan' else 'Sin información' for val in pelicula])

    # Retornar la respuesta formateada
    respuesta = "{} tiene un retorno_total_director de {:,.2f}.".format(nombre_director, total_return)
    respuesta += "\n" + '\n'.join([', '.join(pelicula) for pelicula in detalles_peliculas_str])
    return respuesta

