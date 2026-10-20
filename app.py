# desenvolver um backend com API -
# postman - testes http -> verificar respostas da API
# 1. OBJETIVO
# 2. URLBASE
# 3. ENDPOINTS
# 4. RECURSOS DISPONIBILIZADOS

# VAMOS CRIAR UMA API:
"""
1. CONSULTAR
2. CRIAR
3. EDITAR
4. EXCLUIR
C.R.U.D
"""
from flask import Flask, jsonify, request
app = Flask(__name__)
#APP -> REPRESENTA A APLICAÇÃO FLASK
#__NAME__ INDENTIFICA QUE O MODULO DA APLICAÇÃO

livros = [
    {"id": 1,"titulo": "O Senhor dos Anéis","autor": "J.R.R. Tolkien"},

    {"id": 2,"titulo": "A Revolução dos Bichos","autor": "George Orwell"},

    {"id": 3,"titulo": "A Hipótese do Amor","autor": "Ali Hazelwood"},

    {"id": 4,"titulo": "Harry Potter e a Pedra Filosofal","autor": "J.K. Rowling"},

    {"id": 5,"titulo": "Dom Casmurro","autor": "Machado de Assis"},
    
    {"id": 6,"titulo": "O Pequeno Príncipe","autor": "Antoine de Saint-Exupéry"},

    {"id": 7,"titulo": "A Culpa é das Estrelas","autor": "John Green"},

    {"id": 8,"titulo": "Orgulho e Preconceito","autor": "Jane Austen"},

    {"id": 9,"titulo": "O Hobbit","autor": "J.R.R. Tolkien"},

    {"id": 10,"titulo": "Coraline","autor": "Neil Gaiman"}]

#CONSULTAR LIVROS - CRIAR UMA FUNÇÃO
#def obter_livros():
    #return jsonify(livros)

#CRIAR AS ROTAS /LIVROS
#a rota foi especificada, somente o método GET
#será aceito
@app.route("/livros", methods = ["GET"])
def obter_livros():
    return jsonify(livros)

#CRIAR AS ROTAS /LIVROS ID
@app.route("/livros/<int:id>",methods=["GET"])
#<int:> indica inteiro
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({"message": "LIVRO NAO ENCONTRADO"}), 404

#PUT-> primeiro, os dados enviados pelo Cliente serão obtidos
@app.route("/livros/<int:id>", methods=["PUT"])
def editar_livros_por_id(id):
    #permite acessar os dados json enviados no corpo da requisição
    livros_alterado =request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get("get")==id:
            livros[indice].update(livro_alterado)
            return jsonify(livro[indice])
        
@app.route("/livros", methods=["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    #como é necessario remover o elemento da liste pelo seu indice, será utulizado novamente o enumerate()
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros.pop(indice)
            return jsonify(livros)

#INICIALIZAÇÃO DO SERVIDOR LOCAL
app.run(
    host="localhost",
    port=5001,
    debug=True
)