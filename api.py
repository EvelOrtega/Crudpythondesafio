from crypt import methods
from email.mime import application
from urllib import response
from clientes import *


#rota para mostrar todos os clientes
@app.route('/clientes', methods=['GET'])
def get_clientes():
    return jsonify({'Clientes': Cliente.get_all_clientes()})

#rota para bucar cliente por id
@app.route('/clientes/<int:id>', methods=['GET'])
def get_cliente_by_id(id):
    return_value = Cliente.get_cliente(id)
    return jsonify(return_value)

#rota para criação de clientes
@app.route('/clientes', methods=['POST'])
def add_cliente():
    request_data = request.get_json()
    Cliente.add_cliente(request_data['nome'], request_data['telefone'], request_data['eMail'], request_data['motivoContato'])
    response = Response('Cliente Adicionado com sucesso!', 201, mimetype='application/json')
    return response


#rotas opicionais(extras)

#atualizar
@app.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    
    request_data = request.get_json()
    Cliente.update_cliente(id, request_data['nome'], request_data['telefone'], request_data['eMail'], request_data['motivoContato'])
    response = Response("Cliente", status=200, mimetype='application/json')
    return response

#Deletar
@app.route('/clientes/<int:id>', methods=['DELETE'])
def remover_cliente(id):
    
    Cliente.delete_cliente(id)
    response = Response("Cliente Deletado", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)