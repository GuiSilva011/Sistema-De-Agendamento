from flask import Flask, jsonify, request
from sistema import listar_agendamentos, cadastrar_agendamento

app = Flask(__name__)

@app.route("/agendamentos", methods=["GET"])
def get_agendamentos():
    data = request.args.get("data")
    return jsonify(listar_agendamentos(data))

@app.route("/agendamentos", methods=["POST"])
def post_agendamento():
    dados = request.json
    cadastrar_agendamento(
        dados["nome"],
        dados["email"],
        dados["telefone"],
        dados["servico"],
        dados["data"],
        dados["hora"]
    )
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)