import pandas as pd


def peliculas_pais(Pais: str,):

    df_countries = pd.read_parquet('datasets/pq_countries.parquet')

    # Buscar la fila correspondiente al país en el DataFrame
    country_row = df_countries[df_countries['countries_keys'] == Pais]

    if not country_row.empty:
        Z = country_row['countries_keys'].values[0]
        X = country_row['productions'].values[0]
        Y = country_row['countries'].values[0]
        mensaje = f"Se produjeron {X} películas en el país {Z} ({Y})"
        return mensaje
    else:
        return "País no encontrado en el DataFrame"


# Ejemplo de uso
pais = 'US'  # País que deseas consultar
mensaje_resultado = peliculas_pais(pais)
print(mensaje_resultado)

pais2 = 'AR'  # País que deseas consultar
mensaje_resultado2 = peliculas_pais(pais2)
print(mensaje_resultado2)