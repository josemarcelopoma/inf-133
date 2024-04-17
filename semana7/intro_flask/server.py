from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

@app.route("/saludar", methods=["GET"])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

@app.route("/sumar", methods=["GET"])
def sumar():
    numero1 = request.args.get("numero1")
    numero2 = request.args.get("numero2")
    if not numero1 or not numero2:
        return (
            jsonify({"error": "Se requieren ambos números en los parámetros de la URL."}),
            400,
        )
    try:
        resultado = int(numero1) + int(numero2)
        return jsonify({"resultado": resultado})
    except ValueError:
        return (
            jsonify({"error": "Los parámetros deben ser números enteros."}),
            400,
        )



@app.route("/palindromo", methods=["GET"])
def palindromo():
    cadena = request.args.get("cadena")
    if not cadena:
        return (
            jsonify({"error": "Se requiere una cadena en los parámetros de la URL."}),
            400,
        )
    if cadena == cadena[::-1]:
        return jsonify({"palindromo": True})
    else:
        return jsonify({"palindromo": False})




@app.route("/contar", methods=["GET"])
def contar():
    cadena = request.args.get("cadena")
    vocal = request.args.get("vocal")
    if not cadena or not vocal:
        return (
            jsonify({"error": "Se requiere una cadena y una vocal en los parámetros de la URL."}),
            400,
        )
    count = cadena.lower().count(vocal.lower())
    return jsonify({"cantidad": count})

if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run()