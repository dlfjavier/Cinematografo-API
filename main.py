from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Ejemplo de DataFrame con los datos de películas
df_peliculas = pd.DataFrame({
    'belongs_to_collection': ['Colección 1', 'Colección 2', None],
    'budget': [1000000, 2000000, 1500000],
    'genres': ['Acción', 'Drama', 'Comedia'],
    'id': [1, 2, 3],
    'original_language': ['es', 'en', 'fr'],
    'overview': ['Resumen película 1', 'Resumen película 2', 'Resumen película 3'],
    'popularity': [8.2, 7.5, 9.0],
    'production_companies': ['Compañía 1', 'Compañía 2', 'Compañía 3'],
    'production_countries': ['País 1', 'País 2', 'País 3'],
    'release_date': ['2022-01-01', '2021-02-01', '2023-03-01'],
    'revenue': [5000000, 4000000, 6000000],
    'runtime': [120, 90, 105],
    'spoken_languages': ['Español', 'Inglés', 'Francés'],
    'status': ['Released', 'Released', 'Released'],
    'tagline': ['Tagline 1', 'Tagline 2', 'Tagline 3'],
    'title': ['Película 1', 'Película 2', 'Película 3'],
    'vote_average': [7.9, 6.8, 8.5],
    'vote_count': [2000, 300, 2500],
    'jacc_args_Genres': [0.5, 0.6, 0.7],
    'release_year': [2022, 2021, 2023],
    'return': [3000000, 1000000, 4000000]
})

df_credits = pd.DataFrame({
    'actor': ['Pacino', 'Strip', 'DeNiro'],
    'director': ['Coppola', 'Allen', 'Stone'],
    'id': [1, 2, 3]
})

df_peliculas['release_date'] = pd.to_datetime(df_peliculas['release_date'])

@app.get("/index/")
def index():
    cfun1 = ["para retornar la cantidad de peliculas que se estrenaron ese mes historicamente /cantidad_filmaciones_mes/{mes}"]
    cfun2 = ["para retornar la cantidad de peliculas que se estrenaron ese dia historicamente /cantidad_filmaciones_dia{dia}"]
    cfun3 = ["ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score /score_titulo/{titulo}"]
    cfun4 = ["ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones /votos_titulo/{titulo}"]
    cfun5 = ["ingresa nombre de actor para devolver el éxito a través del retorno y cantidad de películas que participó y el promedio de retorno /get_actor/{nombre_actor"]  
    cfun6 = ["ingresa nombre de director para devolver el éxito del mismo medido a través del retorno, nombre de sus películas, "]
    cfun6 = cfun6 + ["con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. /get_director(nombre_director)"]
    cfun7 = ['Ingresas un nombre de pelicula y te recomienda las similares en una lista. /recomendacion/{titulo}']

    milista = cfun1+cfun2+cfun3+cfun4+cfun5+cfun6+cfun7
    return milista

@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    meses_ingles = {
        'enero': 'January',
        'febrero': 'February',
        'marzo': 'March',
        'abril': 'April',
        'mayo': 'May',
        'junio': 'June',
        'julio': 'July',
        'agosto': 'August',
        'septiembre': 'September',
        'octubre': 'October',
        'noviembre': 'November',
        'diciembre': 'December',
    }
    mes_ingles = meses_ingles.get(mes.lower())

    cantidad = len(df_peliculas[df_peliculas["release_date"].dt.month_name().str.lower() == mes_ingles.lower()])
    if cantidad == 0:
        return f"no fueron estrenadas películas en el mes de {mes.capitalize()}"
    elif cantidad == 1:
        return f"una película fue estrenada en el mes de {mes.capitalize()}"
    else:
        return f"{cantidad} cantidad de películas fueron estrenadas en el mes de {mes.capitalize()}"

@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia: str):
    dias_ingles = {
        'lunes': 'Monday',
        'martes': 'Tuesday',
        'miercoles': 'Wednesday',
        'jueves': 'Thursday',
        'viernes': 'Friday',
        'sabado': 'Saturday',
        'domingo': 'Sunday',
    }
    dia_ingles = dias_ingles.get(dia.lower())
    cantidad = len(df_peliculas[df_peliculas["release_date"].dt.day_name().str.lower() == dia_ingles.lower()])
    if cantidad == 0:
        return f"no fueron estrenadas películas los días {dia.capitalize()}"
    elif cantidad == 1:
        return f"una película fue estrenada los días {dia.capitalize()}"
    else:
        return f"{cantidad} cantidad de películas fueron estrenadas los días {dia.capitalize()}"


@app.get("/score_titulo/{titulo}")
def score_titulo(titulo: str):
    pelicula = df_peliculas[df_peliculas["title"] == titulo].iloc[0]
    return f"La película {pelicula['title']} fue estrenada en el año {pelicula['release_year']} con un score/popularidad de {pelicula['popularity']}"

@app.get("/votos_titulo/{titulo}")
def votos_titulo(titulo: str):
    pelicula = df_peliculas[df_peliculas["title"] == titulo].iloc[0]
    if pelicula["vote_count"] >= 2000:
        return f"La película {pelicula['title']} fue estrenada en el año {pelicula['release_year']}. La misma cuenta con un total de {pelicula['vote_count']} valoraciones, con un promedio de {pelicula['vote_average']}"
    else:
        return f"La película {pelicula['title']} no cumple con la condición de tener al menos 2000 valoraciones."

@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor: str):
    actor_films = df_credits[df_credits['actor'] == nombre_actor]
    actor_films_ids = actor_films['id'].tolist()

    actor_movies = df_peliculas[df_peliculas['id'].isin(actor_films_ids)]
    cantidad_filmaciones = len(actor_movies)
    
    if cantidad_filmaciones == 0:
        mensaje = f"No se encontraron películas que actúe {nombre_actor}."
    else:
        mensaje = f"{nombre_actor} ha participado en {cantidad_filmaciones} filmaciones. Ha conseguido un retorno total de {actor_movies['return'].sum()} con un promedio de {actor_movies['return'].sum() / cantidad_filmaciones} por filmación."
    return mensaje

@app.get("/get_director/{nombre_director}")
def get_director(nombre_director: str):
    director_films = df_credits[df_credits['director'] == nombre_director]
    director_films_ids = director_films['id'].tolist()

    director_movies = df_peliculas[df_peliculas['id'].isin(director_films_ids)]
    peliculas_info = []

    if director_movies.empty:
        mensaje = f"No se encontraron películas dirigidas por {nombre_director}."
    else:
        for index, row in director_movies.iterrows():
            pelicula_info = {
                'nombre_película': row['title'],
                'fecha_lanzamiento': row['release_date'],
                'retorno_individual': row['return'],
                'costo': row['budget'],
                'ganancia': row['revenue']
            }
            peliculas_info.append(pelicula_info)

        mensaje = f"El director {nombre_director} ha tenido éxito con las siguientes películas:\n"
        for pelicula in peliculas_info:
            mensaje += f"Nombre: {pelicula['nombre_película']}\n"
            mensaje += f"Fecha de lanzamiento: {pelicula['fecha_lanzamiento']}\n"
            mensaje += f"Retorno individual: {pelicula['retorno_individual']}\n"
            mensaje += f"Costo: {pelicula['costo']}\n"
            mensaje += f"Ganancia: {pelicula['ganancia']}\n\n"

    return mensaje

