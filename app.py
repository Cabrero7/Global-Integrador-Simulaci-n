from flask import Flask, render_template, request
from generadorNumeros import generador_mixto, generador_multiplicativo, generador_bits_sistema
from chi_cuadrada import validar_chi_cuadrada
from validaciones_extras import calcular_entropia

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        tipo = request.form["tipo"]
        cantidad = int(request.form["cantidad"])
        alpha = float(request.form["alpha"])
        intervalos = int(request.form["intervalos"])

        if tipo == "mixto":
            a = int(request.form["a"])
            b = int(request.form["b"])
            m = int(request.form["m"])
            semilla = int(request.form["semilla"])
            numeros = generador_mixto(a, b, m, semilla, cantidad)

        elif tipo == "multiplicativo":
            a = int(request.form["a"])
            m = int(request.form["m"])
            semilla = int(request.form["semilla"])
            numeros = generador_multiplicativo(a, m, semilla, cantidad)

        else:
            numeros = generador_bits_sistema(cantidad)

        chi = validar_chi_cuadrada(numeros, intervalos, alpha)
        entropia = calcular_entropia(numeros)

        resultado = {
            "numeros": numeros[:10],  # mostramos solo los primeros
            "chi": chi,
            "entropia": entropia
        }

    return render_template("index.html", resultado=resultado)
    
if __name__ == "__main__":
    app.run(debug=True)
