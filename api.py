from flask import Flask, request, jsonify
import random
import string

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Função para gerar o token
def gerar_token(nome):
    comprimento = random.randint(5, 7)  
    caracteres = string.ascii_uppercase + string.digits  
    token = ''.join(random.choice(caracteres) for _ in range(comprimento))  
    return token

# Rota para gerar o token
@app.route('/gerar-token', methods=['POST'])
def gerar_token_endpoint():
    # Obtém o nome enviado no corpo da requisição
    data = request.get_json()
    nome = data.get('nome')

    if not nome:
        return jsonify({"error": "Nome não fornecido"}), 400

    # Gera o token
    token = gerar_token(nome)

    return jsonify({"token": token})

if __name__ == "__main__":
    app.run(debug=True)