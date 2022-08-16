from configs import *
import json


#inicializando
db = SQLAlchemy(app)

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    eMail = db.Column(db.String(80), nullable=False)
    motivoContato = db.Column(db.String(500), nullable=False)

    def json(self):
        return {'id':self.id, 'nome':self.nome,'telefone':self.telefone,'eMail':self.eMail, 'motivoContato':self.motivoContato}

    def add_cliente(_nome, _telefone, _eMail, _motivoContato):
        novo_cliente = Cliente(nome=_nome, telefone=_telefone, eMail =_eMail, motivoContato=_motivoContato)
        db.session.add(novo_cliente)
        db.session.commit()

    def get_all_clientes():
        return [Cliente.json(cliente) for cliente in Cliente.query.all()]

    def get_cliente(_id):
        return [Cliente.json(Cliente.query.filter_by(id=_id).first())]

    # opicionais, afinal se chama CRUD Create, Read, Update e Delete, vou fazer por fazer rssss

    def update_cliente(_id, _nome, _telefone, _eMail, _motivoContato):
        cliente_para_atualizar = Cliente.query.filter_by(id=_id)
        cliente_para_atualizar.nome = _nome
        cliente_para_atualizar.telefone = _telefone
        cliente_para_atualizar.eMail= _eMail
        cliente_para_atualizar.motivoContato = _motivoContato
        db.session.commit()

    def delete_cliente(_id):
        Cliente.query.filter_by(id=_id).delete()
        db.session.commit()
        