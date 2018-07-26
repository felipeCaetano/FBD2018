from flask import Flask


fabrica_de_roupas = Flask(__name__)

fabrica_de_roupas.config.from_object('config') #lendo o arqivo de config

from app.controllers import default
