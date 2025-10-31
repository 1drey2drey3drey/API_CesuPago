from flask import Flask, jsonify, request
from banco import CesuPago

app = Flask(__name__)
banco = CesuPago()


@app.route("/criar_conta", methods=["POST"])
def criar_conta():
    data = request.get_json()
    nome_cliente = data.get("nome_cliente")

    if not nome_cliente:
        return jsonify({"erro": "Nome do cliente é obrigatório"}), 400

    novo_id = str(len(banco.contas) + 1).zfill(3)
    resultado = banco.cadastrar_conta(novo_id, nome_cliente)
    return jsonify({"mensagem": resultado}), 201



@app.route("/contas", methods=["GET"])
def listar_contas():
    return jsonify(banco.contas)


# Ver saldo (GET)
@app.route("/saldo/<id_conta>", methods=["GET"])
def saldo(id_conta):
    resultado = banco.ver_saldo(id_conta)
    return jsonify({"saldo": resultado})


# Depositar (PUT)
@app.route("/depositar/<id_conta>", methods=["PUT"])
def depositar(id_conta):
    data = request.get_json()
    valor = data.get("valor")

    if valor is None:
        return jsonify({"erro": "Informe o valor do depósito"}), 400

    resultado = banco.depositar(id_conta, valor)
    return jsonify({"mensagem": resultado})


# Sacar (PUT)
@app.route("/sacar/<id_conta>", methods=["PUT"])
def sacar(id_conta):
    data = request.get_json()
    valor = data.get("valor")

    if valor is None:
        return jsonify({"erro": "Informe o valor do saque"}), 400

    resultado = banco.sacar(id_conta, valor)
    return jsonify({"mensagem": resultado})


# Extrato (GET)
@app.route("/extrato/<id_conta>", methods=["GET"])
def extrato(id_conta):
    resultado = banco.ver_extrato(id_conta)
    return jsonify({"extrato": resultado})

# (Filipe) Adicionei rota pra cadastrar a chave Pix
@app.route("/pix/cadastrar/<id_conta>", methods=["POST"])
def cadastrar_pix(id_conta):
    resultado, status_code = banco.cadastrar_chave_pix(id_conta)
    return jsonify(resultado), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
