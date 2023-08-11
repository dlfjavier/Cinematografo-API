import pandas as pd

def franquicia(Franquicia: str):
    df_collections = pd.read_parquet('pq_collections.parquet')
    franquicia_data = df_collections[df_collections['collection'] == Franquicia]
    movies_count = franquicia_data['title'].count()
    total_revenue = franquicia_data['revenue'].sum()

    if movies_count > 0:
        average_revenue = total_revenue / movies_count
    else:
        average_revenue = 0

    total_revenueF = "{:,.2f}".format(total_revenue)
    average_revenueF = "{:,.2f}".format(average_revenue)
    return f"La franquicia {Franquicia} posee {movies_count} películas, una ganancia total de {total_revenueF} y una ganancia promedio de {average_revenueF}"


# Ejemplo de uso:
franquicia_info = franquicia('The Neverending Story Collection')
franquicia_info2 = franquicia('Batman Collection')
print(franquicia_info)

print(franquicia_info2)