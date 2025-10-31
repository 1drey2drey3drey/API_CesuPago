# 💳 CesuPago API

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Latest-green)
![Status](https://img.shields.io/badge/Status-Online-success)

**CesuPago** é uma API REST completa para gerenciamento de contas bancárias digitais. Oferece funcionalidades essenciais como criação de contas, transações financeiras (depósitos e saques), consultas de saldo e extrato, além de integração com o sistema PIX para transferências instantâneas.

## 🌐 Base URL

```
https://cesupago.onrender.com
```

## 📚 Documentação Completa

Acesse a documentação interativa no Postman:
👉 [CesuPago API - Postman Documentation](https://documenter.getpostman.com/view/49143887/2sB3QKsqfD)

---

## 🎯 Funcionalidades

- ✅ **Gerenciamento de Contas**: Criar e listar contas bancárias
- 💰 **Consulta de Saldo**: Verificar saldo disponível em tempo real
- 💵 **Depósitos**: Adicionar fundos às contas
- 💸 **Saques**: Retirar valores com validação de saldo
- 📜 **Extrato Bancário**: Histórico completo de transações
- 🔑 **Sistema PIX**: Cadastro de chaves aleatórias para transferências

---

## 📋 Endpoints da API

### 1️⃣ Criar Conta Bancária

Cria uma nova conta com saldo inicial de **R$ 100,00**.

```http
POST /criar_conta
Content-Type: application/json
```

**Request Body:**
```json
{
  "nome_cliente": "Maria Silva"
}
```

**Response Success (201):**
```json
{
  "mensagem": "Conta 002 criada para Maria Silva."
}
```

**Response Error (400):**
```json
{
  "erro": "Nome do cliente é obrigatório"
}
```

**Exemplo cURL:**
```bash
curl -X POST https://cesupago.onrender.com/criar_conta \
  -H "Content-Type: application/json" \
  -d '{"nome_cliente": "Maria Silva"}'
```

---

### 2️⃣ Listar Todas as Contas

Retorna a lista completa de contas cadastradas no sistema.

```http
GET /contas
```

**Response Success (200):**
```json
[
  {
    "id": "001",
    "nome_cliente": "Everton",
    "saldo": 100.0,
    "extrato": [
      "Abertura da conta (saldo inicial: 100.0)"
    ],
    "chave_pix": null
  },
  {
    "id": "002",
    "nome_cliente": "Maria Silva",
    "saldo": 350.75,
    "extrato": [
      "Abertura da conta (saldo inicial: 100.0)",
      "Depósito de 250.75 | Saldo: 350.75"
    ],
    "chave_pix": "a3f5c8d9-1234-5678-9abc-def012345678"
  }
]
```

**Exemplo cURL:**
```bash
curl https://cesupago.onrender.com/contas
```

---

### 3️⃣ Consultar Saldo

Verifica o saldo atual de uma conta específica.

```http
GET /saldo/{id_conta}
```

**Parâmetros:**
- `id_conta` (path): ID da conta (ex: 001, 002)

**Response Success (200):**
```json
{
  "saldo": "Saldo da conta 001: 350.75"
}
```

**Response Error:**
```json
{
  "saldo": "Conta não encontrada."
}
```

**Exemplo cURL:**
```bash
curl https://cesupago.onrender.com/saldo/001
```

---

### 4️⃣ Realizar Depósito

Adiciona fundos a uma conta bancária.

```http
PUT /depositar/{id_conta}
Content-Type: application/json
```

**Parâmetros:**
- `id_conta` (path): ID da conta

**Request Body:**
```json
{
  "valor": 500.00
}
```

**Response Success (200):**
```json
{
  "mensagem": "Depósito de 500.00 realizado na conta 001."
}
```

**Response Error (400):**
```json
{
  "erro": "Informe o valor do depósito"
}
```

**Validações:**
- ✅ Valor deve ser numérico
- ✅ Valor deve ser positivo (> 0)

**Exemplo cURL:**
```bash
curl -X PUT https://cesupago.onrender.com/depositar/001 \
  -H "Content-Type: application/json" \
  -d '{"valor": 500.00}'
```

---

### 5️⃣ Realizar Saque

Retira fundos de uma conta bancária.

```http
PUT /sacar/{id_conta}
Content-Type: application/json
```

**Parâmetros:**
- `id_conta` (path): ID da conta

**Request Body:**
```json
{
  "valor": 150.00
}
```

**Response Success (200):**
```json
{
  "mensagem": "Saque de 150.00 realizado na conta 001."
}
```

**Response Error - Saldo Insuficiente:**
```json
{
  "mensagem": "Saldo insuficiente."
}
```

**Response Error (400):**
```json
{
  "erro": "Informe o valor do saque"
}
```

**Validações:**
- ✅ Valor deve ser numérico
- ✅ Valor deve ser positivo (> 0)
- ✅ Saldo deve ser suficiente para o saque

**Exemplo cURL:**
```bash
curl -X PUT https://cesupago.onrender.com/sacar/001 \
  -H "Content-Type: application/json" \
  -d '{"valor": 150.00}'
```

---

### 6️⃣ Visualizar Extrato

Retorna o histórico completo de transações da conta.

```http
GET /extrato/{id_conta}
```

**Parâmetros:**
- `id_conta` (path): ID da conta

**Response Success (200):**
```json
{
  "extrato": "Extrato da conta 001:\nAbertura da conta (saldo inicial: 100.0)\nDepósito de 500.00 | Saldo: 600.00\nSaque de 150.00 | Saldo: 450.00"
}
```

**Response Error:**
```json
{
  "extrato": "Conta não encontrada."
}
```

**Exemplo cURL:**
```bash
curl https://cesupago.onrender.com/extrato/001
```

---

### 7️⃣ Cadastrar Chave PIX

Gera e cadastra uma chave PIX aleatória (formato UUID) para a conta.

```http
POST /pix/cadastrar/{id_conta}
```

**Parâmetros:**
- `id_conta` (path): ID da conta

**Response Success (201):**
```json
{
  "mensagem": "Chave PIX aleatória cadastrada com sucesso!",
  "conta": "001",
  "chave_pix": "a3f5c8d9-1234-5678-9abc-def012345678"
}
```

**Response Error - Chave Já Existe (409):**
```json
{
  "erro": "A conta 001 já possui uma chave PIX cadastrada."
}
```

**Response Error - Conta Não Encontrada (404):**
```json
{
  "erro": "Conta não encontrada."
}
```

**Exemplo cURL:**
```bash
curl -X POST https://cesupago.onrender.com/pix/cadastrar/001
```

---

## 🔄 Fluxo Completo de Uso

Aqui está um exemplo prático de uso completo da API:

```bash
# 1️⃣ Criar uma nova conta
curl -X POST https://cesupago.onrender.com/criar_conta \
  -H "Content-Type: application/json" \
  -d '{"nome_cliente": "João Pedro"}'

# 2️⃣ Listar todas as contas
curl https://cesupago.onrender.com/contas

# 3️⃣ Consultar saldo inicial
curl https://cesupago.onrender.com/saldo/002

# 4️⃣ Realizar um depósito
curl -X PUT https://cesupago.onrender.com/depositar/002 \
  -H "Content-Type: application/json" \
  -d '{"valor": 1000}'

# 5️⃣ Cadastrar chave PIX
curl -X POST https://cesupago.onrender.com/pix/cadastrar/002

# 6️⃣ Fazer um saque
curl -X PUT https://cesupago.onrender.com/sacar/002 \
  -H "Content-Type: application/json" \
  -d '{"valor": 250}'

# 7️⃣ Verificar extrato completo
curl https://cesupago.onrender.com/extrato/002
```

---

## 🐍 Exemplo em Python

```python
import requests

BASE_URL = "https://cesupago.onrender.com"

# Criar uma nova conta
response = requests.post(
    f"{BASE_URL}/criar_conta",
    json={"nome_cliente": "Ana Carolina"}
)
print(response.json())

# Consultar saldo
response = requests.get(f"{BASE_URL}/saldo/003")
print(response.json())

# Fazer depósito
response = requests.put(
    f"{BASE_URL}/depositar/003",
    json={"valor": 750.50}
)
print(response.json())

# Cadastrar PIX
response = requests.post(f"{BASE_URL}/pix/cadastrar/003")
print(response.json())

# Fazer saque
response = requests.put(
    f"{BASE_URL}/sacar/003",
    json={"valor": 200}
)
print(response.json())

# Ver extrato
response = requests.get(f"{BASE_URL}/extrato/003")
print(response.json())
```

---

## 💻 Exemplo em JavaScript (Node.js)

```javascript
const axios = require('axios');

const BASE_URL = 'https://cesupago.onrender.com';

// Criar conta
async function criarConta() {
  const response = await axios.post(`${BASE_URL}/criar_conta`, {
    nome_cliente: 'Carlos Eduardo'
  });
  console.log(response.data);
}

// Depositar
async function depositar(idConta, valor) {
  const response = await axios.put(`${BASE_URL}/depositar/${idConta}`, {
    valor: valor
  });
  console.log(response.data);
}

// Executar
criarConta();
depositar('001', 300);
```

---

## 📊 Códigos de Status HTTP

| Código | Descrição |
|--------|-----------|
| **200** | Requisição bem-sucedida |
| **201** | Recurso criado com sucesso |
| **400** | Requisição inválida (dados faltando ou inválidos) |
| **404** | Recurso não encontrado |
| **409** | Conflito (chave PIX já cadastrada) |

---

## 🎲 Regras de Negócio

### Criação de Contas
- ✅ Toda conta nova recebe **R$ 100,00** de saldo inicial
- ✅ ID da conta é gerado automaticamente de forma sequencial (001, 002, 003...)
- ✅ Nome do cliente é obrigatório

### Depósitos
- ✅ Valor deve ser numérico e positivo
- ✅ Não há limite máximo para depósitos
- ✅ Todas as transações são registradas no extrato

### Saques
- ✅ Valor deve ser numérico e positivo
- ✅ Saldo deve ser suficiente para realizar o saque
- ✅ Não é permitido ficar com saldo negativo

### Chave PIX
- ✅ Cada conta pode ter apenas **uma chave PIX**
- ✅ A chave é gerada automaticamente no formato UUID
- ✅ Não é possível alterar a chave após o cadastro

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|------------|-----------|
| **Python 3.x** | Linguagem de programação |
| **Flask** | Framework web para API REST |
| **UUID** | Geração de identificadores únicos para PIX |
| **Render** | Plataforma de hospedagem cloud |

---

## 📁 Estrutura do Projeto

```
cesupago/
│
├── app.py              # Rotas da API (endpoints)
├── banco.py            # Lógica de negócio (classe CesuPago)
├── contas.py           # Dados iniciais das contas
├── README.md           # Documentação (este arquivo)
└── requirements.txt    # Dependências do projeto
```

---

## 🧪 Testando a API

### Postman
1. Acesse a [documentação no Postman](https://documenter.getpostman.com/view/49143887/2sB3QKsqfD)
2. Clique em "Run in Postman" para importar a coleção
3. Configure a variável de ambiente `base_url` para `https://cesupago.onrender.com`
4. Execute as requisições

### Insomnia
1. Crie uma nova requisição
2. Configure o método HTTP (GET, POST, PUT)
3. Insira a URL completa do endpoint
4. Adicione o body (quando necessário)
5. Envie a requisição

### Thunder Client (VS Code)
1. Instale a extensão Thunder Client
2. Crie uma nova requisição
3. Configure método, URL e body
4. Execute

---

## 👥 Equipe de Desenvolvimento

- **Everton** - Desenvolvedor Backend e Arquitetura inicial
- **Filipe** - Implementação do sistema PIX

---

## 🚀 Como Executar Localmente

```bash
# Clone o repositório
git clone https://gitlab.com/grupo-cesupago/cesupago.git
cd cesupago

# Instale as dependências
pip install flask

# Execute a aplicação
python app.py

# Acesse em: http://localhost:5000
```

---

## 📝 Notas Importantes

- 🔒 Esta é uma API de **demonstração educacional**
- ⚠️ **Não utilize em produção** sem implementar:
  - Sistema de autenticação (JWT, OAuth)
  - Autorização e controle de acesso
  - Validação robusta de dados
  - Criptografia de dados sensíveis
  - Rate limiting
  - Logs de auditoria
  - Backup de dados

---

## 📄 Licença

Este projeto é de código aberto para fins educacionais.

---

## 🔗 Links Úteis

- 🌐 **API em Produção**: https://cesupago.onrender.com
- 📖 **Documentação Postman**: https://documenter.getpostman.com/view/49143887/2sB3QKsqfD
- 💻 **Repositório GitLab**: https://gitlab.com/grupo-cesupago/cesupago

---

## 📞 Suporte

Para dúvidas, sugestões ou reportar problemas:
- Abra uma issue no GitLab
- Entre em contato com a equipe de desenvolvimento

---

**🎉 Desenvolvido com 💙 pela equipe CesuPago**