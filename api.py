from flask import Flask, request, jsonify
import random
import string

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def gerar_token(nome):
    comprimento = random.randint(5, 7)  
    caracteres = string.ascii_uppercase + string.digits  
    token = ''.join(random.choice(caracteres) for _ in range(comprimento))  
    return token


@app.route('/gerar-token', methods=['POST'])
def gerar_token_endpoint():
    data = request.get_json()
    nome = data.get('nome')

    if not nome:
        return jsonify({"error": "Nome não fornecido"}), 400

    token = gerar_token(nome)

    return jsonify({"token": token})

if __name__ == "__main__":
    app.run(debug=True)