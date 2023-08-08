from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/consulta", methods=["POST"])
def consulta():
    funcion = request.form["funcion"]
    argumento = request.form["argumento"]

    if funcion == "peliculas_idioma":
        response = requests.get(f"https://drat-api.onrender.com/peliculas_idioma/{argumento}")
    elif funcion == "peliculas_duracion":
        response = requests.get(f"https://drat-api.onrender.com/peliculas_duracion/{argumento}")
    elif funcion == "franquicia":
        response = requests.get(f"https://drat-api.onrender.com/franquicia/{argumento}")
    elif funcion == "peliculas_pais":
        response = requests.get(f"https://drat-api.onrender.com/peliculas_pais/{argumento}")
    elif funcion == "productoras_exitosas":
        response = requests.get(f"https://drat-api.onrender.com/productoras_exitosas/{argumento}")
    elif funcion == "get_director":
        response = requests.get(f"https://drat-api.onrender.com/get_director/{argumento}")
    elif funcion == "recomendacion":
        response = requests.get(f"https://drat-api.onrender.com/recomendacion/{argumento}")
    else:
        return "Función no reconocida"

    result = response.text
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
