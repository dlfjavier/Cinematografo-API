import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity


def recomendacion(titulo: str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
    # Leer el archivo CSV y convertirlo en un DataFrame
    df = pd.read_parquet('datasets/pq_reccom.parquet')

    search_word = titulo
    # Crear un nuevo dataframe df_movies_final eliminando las filas con budget igual a 0
    #df_movies_final = df_movies[df_movies['budget'] != 0]

    # Función para realizar el entrenamiento y obtener las recomendaciones
    def get_recommendations(search_word, df):
        # Crear una matriz TF-IDF para representar los títulos de las películas

        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(df['title'])

        # Calcular la similitud coseno entre la búsqueda y los títulos de las películas
        search_vector = tfidf_vectorizer.transform([search_word])
        similarity_scores = cosine_similarity(search_vector, tfidf_matrix).flatten()

        # Agregar los resultados al dataframe y ordenarlos por puntuación en forma descendente
        df['score'] = similarity_scores
        df = df.sort_values(by='score', ascending=False)

        # Filtrar los 5 primeros resultados y agregarlos al diccionario de resultados
        result_dict = {}
        for i in range(5):
            result_dict[df.iloc[i]['title']] = df.iloc[i]['score']

        return result_dict

    # Realizar la búsqueda y obtener los resultados para la palabra clave 'Live'
    # search_word = titulo
    dic_resultado = get_recommendations(search_word, df)

    # Mostrar los resultados
    total = sum(dic_resultado.values())

    dic_resultado = {'No se encontaron resultado'} if total == 0 else dic_resultado

    dic_resultado = dic_resultado if total > 0 else {'No se encontaron resultado'}

    return dic_resultado

'''df = pd.read_parquet('datasets/pq_reccom.parquet')
print(df)'''
print(recomendacion('Spider Man'))