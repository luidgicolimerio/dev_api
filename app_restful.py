from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Luidgi',
        'habilidades': ['Python', 'Flask']},
    {
        'id': 1,
        'nome': 'Rodrigo',
        'habilidades': ['Python', 'Django']},
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'status': 'error', 'mensagem': mensagem }
        return response
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro excluído'}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/devs/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)

