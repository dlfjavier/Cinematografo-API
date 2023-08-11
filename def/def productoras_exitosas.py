import pandas as pd

def productoras_exitosas(Productora: str):
    # Cargar el DataFrame desde el archivo 'pq_prodCo.parquet'
    df_prodCo = pd.read_parquet('datasets/pq_prodCo.parquet')

    # Filtrar el DataFrame para obtener las filas donde la columna 'companies' sea igual al valor de la productora
    filtro = df_prodCo['companies'] == Productora
    resultado = df_prodCo[filtro]

    # Verificar si se encontraron resultados para la productora
    if resultado.empty:
        print(f"No se encontraron datos para la productora '{Productora}'")
        return None
    else:
    # Obtener los valores de 'total_revenue' y 'total_movies' para la productora
        total_revenue_resultado = "{:,.2f}".format(resultado['total_revenue'].values[0])
        total_movies_resultado = resultado['total_movies'].values[0]

        return f"La productora {Productora} ha tenido un revenue de {total_revenue_resultado} y ha realizado {total_movies_resultado} películas."

#Ejemplo de uso:
nombre_productora = '100 Bares'# Reemplazar por el nombre de la productora a consultar
resultado = productoras_exitosas(nombre_productora)
print(resultado)

nombre_productora1 = 'Pixar Animation Studios'#  Reemplazar por el nombre de la productora a consultar
resultado1 = productoras_exitosas(nombre_productora1)
print(resultado1)

print(pd.read_parquet('datasets/pq_prodCo.parquet').columns)