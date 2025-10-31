from contas import contas
import uuid

class CesuPago:
    def __init__(self):
        self.contas = contas

    def cadastrar_conta(self, id_conta, nome_cliente):
        for c in self.contas:
            if c["id"] == id_conta:
                return f"❌ Já existe uma conta com ID {id_conta}."
        nova = {
            "id": id_conta,
            "nome_cliente": nome_cliente,
            "saldo": 100.0,
            "extrato": ["Abertura da conta (saldo inicial: 100.0)"],
            "chave_pix": None  # cadastrar a chave Pix
        }
        self.contas.append(nova)
        return f"Conta {id_conta} criada para {nome_cliente}."

    def listar_contas(self):
        if not self.contas:
            return "Nenhuma conta cadastrada."
        linhas = []
        for c in self.contas:
            linhas.append(f"ID: {c['id']} | Cliente: {c['nome_cliente']} | Saldo: {c['saldo']:.2f}")
        return "\n".join(linhas)

    def ver_saldo(self, id_conta):
        for c in self.contas:
            if c["id"] == id_conta:
                return f"Saldo da conta {id_conta}: {c['saldo']:.2f}"
        return "Conta não encontrada."

    def depositar(self, id_conta, valor):
        for c in self.contas:
            if c["id"] == id_conta:
                try:
                    valor = float(valor)
                except:
                    return "Valor inválido."
                if valor <= 0:
                    return "Valor deve ser positivo."
                c["saldo"] += valor
                c["extrato"].append(f"Depósito de {valor:.2f} | Saldo: {c['saldo']:.2f}")
                return f"Depósito de {valor:.2f} realizado na conta {id_conta}."
        return "❌ Conta não encontrada."

    def sacar(self, id_conta, valor):
        for c in self.contas:
            if c["id"] == id_conta:
                try:
                    valor = float(valor)
                except:
                    return "Valor inválido."
                if valor <= 0:
                    return "Valor deve ser positivo."
                if valor > c["saldo"]:
                    return "Saldo insuficiente."
                c["saldo"] -= valor
                c["extrato"].append(f"Saque de {valor:.2f} | Saldo: {c['saldo']:.2f}")
                return f"Saque de {valor:.2f} realizado na conta {id_conta}."
        return "Conta não encontrada."

    def ver_extrato(self, id_conta):
        for c in self.contas:
            if c["id"] == id_conta:
                return "Extrato da conta " + id_conta + ":\n" + "\n".join(c["extrato"])
        return "Conta não encontrada."

    # cadastrar uma chave Pix aleatória
    def cadastrar_chave_pix(self, id_conta):
        for c in self.contas:
            if c["id"] == id_conta:
           
                if c.get("chave_pix"):
                    return ({"erro": f"A conta {id_conta} já possui uma chave PIX cadastrada."}, 409)

   
                chave_gerada = str(uuid.uuid4())
                c["chave_pix"] = chave_gerada
                
                mensagem = {
                    "mensagem": "Chave PIX aleatória cadastrada com sucesso!",
                    "conta": id_conta,
                    "chave_pix": chave_gerada
                }
                return (mensagem, 201)
        
        # Se a conta não for encontrada
        return ({"erro": "Conta não encontrada."}, 404)