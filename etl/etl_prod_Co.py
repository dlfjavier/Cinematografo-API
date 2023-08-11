import pandas as pd
import ast
import numpy as np

# Carga el archivo 'movies_dataset.csv' en un DataFrame
df_movies = pd.read_csv('movies_dataset.csv')

#reemplazo de nulos
df_movies['revenue']= df_movies['revenue'].replace(0, np.nan)


# Filtrar el DataFrame original para obtener solo las filas con valor mayor que 0 en la columna "revenue"
df_movies = df_movies[df_movies['revenue'] > 0]

# Paso 2: Desanida la columna 'production_countries' para obtener elementos individuales
df_movies['production_companies'] = df_movies['production_companies'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
df_movies['production_companies_clean'] = df_movies['production_companies'].apply(lambda x: [item['name'] for item in x] if isinstance(x, list) else [])

unique_co = sorted(list(set([item for sublist in df_movies['production_companies_clean'].dropna() for item in sublist])))

# Crear df_prodCo con columna 'companies'
df_prodCo = pd.DataFrame({'companies': unique_co})

# Inicializar las columnas 'total_revenue' y 'total_movies' en df_prodCo con valores cero
df_prodCo['total_revenue'] = 0
df_prodCo['total_movies'] = 0

# Recorrer df_movies y actualizar df_prodCo
for index, movie_row in df_movies.iterrows():
    production_companies = movie_row['production_companies_clean']
    movie_revenue = movie_row['revenue']

    # Verificar si hay más de una compañía en el registro
    if isinstance(production_companies, list):
        companies_list = production_companies
    else:
        companies_list = [production_companies]

    # Actualizar los valores en df_prodCo para cada compañía presente en la película
    for company in companies_list:
        # Filtrar las filas de df_prodCo donde coincida el nombre de la compañía
        company_rows = df_prodCo[df_prodCo['companies'] == company]

        # Sumar el valor de 'revenue' a 'total_revenue' para la compañía actual
        df_prodCo.loc[company_rows.index, 'total_revenue'] += movie_revenue

        # Sumar 1 a 'total_movies' para la compañía actual
        df_prodCo.loc[company_rows.index, 'total_movies'] += 1


def productoras_exitosas(productora: str):
    # Supongamos que ya tienes el DataFrame df_prodCo con las columnas 'companies', 'total_revenue' y 'total_movies'

    # Filtrar el DataFrame para obtener las filas donde la columna 'companies' sea igual al valor de la productora
    filtro = df_prodCo['companies'] == productora
    resultado = df_prodCo[filtro]

    # Verificar si se encontraron resultados para la productora
    if resultado.empty:
        print(f"No se encontraron datos para la productora '{productora}'")
        return None
    else:
    # Obtener los valores de 'total_revenue' y 'total_movies' para la productora
        total_revenue_resultado = resultado['total_revenue'].values[0]
        total_movies_resultado = resultado['total_movies'].values[0]

        return f"La productora {productora} ha tenido un revenue de {total_revenue_resultado} y ha realizado {total_movies_resultado} películas."

df_prodCo.to_parquet('pq_prodCo.parquet', index= False)

'''print(df_prodCo.columns)'''
# Ejemplo de uso:
nombre_productora = "100 Bares"  # Reemplazar por el nombre de la productora que desees consultar
resultado = productoras_exitosas(nombre_productora)
print(resultado)

