import pandas as pd

def peliculas_duracion(Pelicula: str):
    df_runtime = pd.read_parquet('pq_runtime.parquet')
    pelicula_info = df_runtime[df_runtime['title'] == Pelicula]
    if not pelicula_info.empty:
        duracion = pelicula_info['runtime_min'].values[0]
        anio = pelicula_info['year'].values[0]
        return f"{Pelicula}. Duración: {int(duracion)} minutos. Año: {anio}"
    else:
        return f"No se encontró información para la película: {Pelicula}"

# Ejemplo de uso de la función
print(peliculas_duracion('Titanic'))

# /peliculas_duracion/Titanic