from flask import Flask, jsonify


app = Flask(__name__)


continentes = [
    {"id":1, "nombre":"Asia"},
    {"id":2, "nombre":"África"},
    {"id":3, "nombre":"Europa"},
    {"id":4, "nombre":"América"},
    {"id":5, "nombre":"Oceanía"}
]


@app.route("/")
def home():
    return "¡Bienvenido!"


@app.route("/api/continentes", methods=["GET"])
def continente_listar():
    return jsonify(continentes)


@app.route("/api/continentes/<int:id>", methods=["GET"])
def continente_detalle(id):
    continente = None
    for item in continentes:
        if item["id"] == id:
            continente = item
    if continente:
        return jsonify(continente)
    else:
        return jsonify({"error":"No se encuentra el recurso solicitado"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000);
    