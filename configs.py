#importando bibliotecas
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

#instanciando o flask

app = Flask(__name__)

#configuração da database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False