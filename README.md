# PROYECTO INDIVIDUAL Nº1
## Machine Learning Operations (MLOps)

### Descripción del problema:
Se puede leer el contexto y rol a desarrollar en [este enlace](https://github.com/soyHenry/PI_ML_OPS).

### Requerimientos:
- Realizar ETL y EDA sobre los datasets originales.
- Desarrollar una API que pueda ser consumida según los criterios de API REST o RESTful.
- Crear e implementar un modelo de recomendación de películas y 6 funciones para los endpoints que se consumirán en la API.
- Desplegar la API en algún servicio que permita ser utilizada desde la web.

### Resolución:
- Desarrollo en Python.
- Librerias: fastapi, fastparquet, flask, gunicorn, matplotlib, pandas, pyarrow, pydantic, requests, seaborn, scipy, scikit_learn, uvicorn y wordcloud.
- Uso básico de Html y CSS.

### Estructura

draft_Api/
|-- eda.ipynb
|-- main.py (API FastAPI)
|-- requirements.txt (dependencias para la Api)
|-- datasets/
|-- def/
|-- etl/
|-- venv/
|-- front_end/
|   |-- app.py (Frontend Flask)
|   |-- requirements.txt (dependencias para el frontend)
|   |-- templates/
|   |   |-- index.html
|   |-- static/
|       |-- style.css
|-- ...

- `draft_Api/`: directorio raíz del repositorio de GitHub, contiene todos los archivos y carpetas relacionados con el proyecto.
- `eda.ipynb`: análisis exploratorio de los datos (Exploratory Data Analysis-EDA).
- `main.py`: el archivo principal de la API desarrollada con FastAPI, gestiona la aplicación del modelo.
- `requirements.txt`: archivo que tiene las librerías necesarias para ejecutar la API desarrollada con FastAPI.
- `def/`: directorio que contiene archivos .py con los diferentes ensayos de código utilizados para desarrollar las funciones implementadas en los endpoints de la API.
- `datasets/`: directorio que contiene los datasets del proyecto.
- `etl/`: directorio que contiene archivos .py con los diferentes ensayos de código utilizados para realizar la extracción, transformación y carga de datos (Extract, Transform-ETL).
- `venv/`: directorio donde se encuentra el entorno virtual de Python.
- `front_end/`: directorio principal para el front end desarrollado con Flask.
- `front_end/app.py`: archivo principal del front end Flask.
- `front_end/requirements.txt`: archivo que lista las dependencias específicas para el frontend desarrollado con Flask.
- `front_end/templates/`: directorio que contiene las plantillas HTML utilizadas por el frontend Flask.
- `front_end/static/`: directorio que almacena archivos como hojas de estilo CSS utilizadas para dar estilo y funcionalidad a la aplicación web.

### API endpoints
Aplicación desplegada en Render: [https://drat-api.onrender.com](https://drat-api.onrender.com)

- `/peliculas_idioma/{Idioma}`: retorna la cantidad de películas estrenadas en {Idioma}.
- `/peliculas_duracion/{Pelicula}`: retorna duración y el año de estreno de {Pelicula}.
- `/franquicia/{Franquicia}`: retorna la cantidad de películas, ganancia total y promedio de {Franquicia}.
- `/peliculas_pais/{Pais}`: retorna la cantidad de películas producidas en un {Pais}.
- `/productoras_exitosas/{Productora}`: retorna el revenue total y la cantidad de películas que realizó {Productora}.
- `/get_director/{nombre_director}`: retorna el éxito de {nombre_director} a través del retorno y también nombre de sus películas.
- `/recomendacion/{titulo}`: retorna una lista de películas recomendadas similares a {titulo}.

### FrontEnd
Web App de la API desplegada en Render: [https://poryecto-individual-1.onrender.com](https://poryecto-individual-1.onrender.com)

### Extracción, Transformación y Carga (ETL)
En función de consignas y necesidades se llevan a cabo las siguientes operaciones de ETL:
- Se desanidan los campos que tienen como valores en cada fila un diccionario o una lista.
- Se procesan los valores según sea necesario reemplazando o eliminando valores nulos.
- Se crean las columnas requeridas y eliminan las que no serán utilizadas.
- Se obtienen datasets adaptados para cada función con datos procesados.
- Se transforman y guardan los datasets en formato parquet.

### Análisis Exploratorio de Datos (EDA)
En el notebook `eda.ipynb`:
- Se presenta relación entre el revenue total y la cantidad de películas que realizó cada Productora.
- Se realiza un análisis de palabras de la series title y overview.

### Sistema de recomendación
- Se crea una función que a partir del título de una película, retorna una lista de 5 recomendaciones.

### Video de demostración
https://drive.google.com/drive/folders/1EHOI89EIaL26YUpMilQImvau4eQsw9LC?usp=sharing

### Autor
Javier de la Fuente  dlfavier@gmail.com
