import pandas as pd
#import scikit_learn as sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity


def recomendacion0(titulo):
    #dmo
    # Cargar el DataFrame desde el archivo pq_reccom.parquet
    df = pd.read_parquet('datasets/pq_reccom.parquet')
    tfidf = TfidfVectorizer(stop_words="english")
    df['overview'] = df['overview'].fillna("")

    tfidf_matrix = tfidf.fit_transform(df["overview"])
    coseno_sim = linear_kernel(tfidf_matrix,tfidf_matrix)

    indices = pd.Series (df.index, index = df['title']).drop_duplicates()
    idx = indices[titulo]
    idx = min(idx, len(df)-1)
    simil = list(enumerate(coseno_sim[idx]))
    simil = sorted(simil, key= lambda x: x[1], reverse=True)
    simil = simil[1:11]
    movie_index = [df[0] for df in simil]

    lista = df['title'].iloc[movie_index].to_list()[:5]

    return {'list recomendada': lista}

def recomendacion00(titulo):
    #dmo title
    # Cargar el DataFrame desde el archivo pq_reccom.parquet
    df = pd.read_parquet('datasets/pq_reccom10.parquet')
    tfidf = TfidfVectorizer(stop_words="english")
    df['title'] = df['title'].fillna("")

    tfidf_matrix = tfidf.fit_transform(df["title"])
    coseno_sim = linear_kernel(tfidf_matrix,tfidf_matrix)

    indices = pd.Series (df.index, index = df['title']).drop_duplicates()
    idx = indices[titulo]
    idx = min(idx, len(df)-1)
    simil = list(enumerate(coseno_sim[idx]))
    simil = sorted(simil, key= lambda x: x[1], reverse=True)
    simil = simil[1:11]
    movie_index = [df[0] for df in simil]

    lista = df['title'].iloc[movie_index].to_list()[:5]

    return {'Lista recomendada': lista}

def recomendacion(titulo):
    # dlf title
    # Cargar el DataFrame desde el archivo pq_reccom.parquet
    df = pd.read_parquet('datasets/pq_reccom10.parquet')

    # Reemplazar valores nulos en la columna de títulos con una cadena vacía
    df["title"].fillna("", inplace=True)

    if titulo not in df['title'].values:
        return 'No hay recomendación para este título'

    # Crear una matriz TF-IDF de los títulos de las películas
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df["title"])

    # Calcular la similitud coseno entre los títulos
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Obtener el índice de la película proporcionada
    idx = df[df["title"] == titulo].index[0]

    # Obtener los puntajes de similitud de la película proporcionada con todas las demás películas
    similarity_scores = list(enumerate(similarity_matrix[idx]))

    # Ordenar las películas según el puntaje de similitud en orden descendente
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Obtener los títulos de las 5 películas más similares
    top_movies = [df.iloc[score[0]]["title"] for score in similarity_scores[1:6]]

    return top_movies

def recomendacion1(titulo):
    # dlf overview
    # Cargar el DataFrame desde el archivo pq_reccom.parquet
    df = pd.read_parquet('datasets/pq_reccomCol.parquet')

    if titulo not in df['title'].values:
        return 'No hay recomendación para este título'
    # Reemplazar valores nulos en la columna de títulos con una cadena vacía
    df["overview"].fillna("", inplace=True)

    # Crear una matriz TF-IDF de los títulos de las películas
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df["overview"])

    # Calcular la similitud coseno entre los títulos
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Obtener el índice de la película proporcionada
    idx = df[df["title"] == titulo].index[0]

    # Obtener los puntajes de similitud de la película proporcionada con todas las demás películas
    similarity_scores = list(enumerate(similarity_matrix[idx]))

    # Ordenar las películas según el puntaje de similitud en orden descendente
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Obtener los títulos de las 5 películas más similares
    top_movies = [df.iloc[score[0]]["title"] for score in similarity_scores[1:6]]

    return top_movies

hipotesis = 'Spider-Man'
#'Spider-Man'
#'Father of the Bride'

print(recomendacion(hipotesis))
print(recomendacion00(hipotesis))


