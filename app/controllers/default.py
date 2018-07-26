from app import fabrica_de_roupas
from flask import render_template
from flask import request
from flask import flash

"""
Neste arquivo estarão definidas as rotas para o CRUD
"""

#index do projeto
@fabrica_de_roupas.route('/')
def index():
    return render_template('index.html')

#cadastrar
################CADASTRO DE Funcionarios ######################################
@fabrica_de_roupas.route('/cadastrarfuncionarios')
def cadastrar_funcionario():
    return render_template('cadastrarfuncionarios.html')

@fabrica_de_roupas.route('/cadastrar/costureira', methods=["GET", "POST"])
def cadastrar_costureira():
    return render_template('cadastrarfuncionarios.html')

@fabrica_de_roupas.route('/cadastrar/supervisora', methods=["GET", "POST"])
def cadastrar_supervisora():
    return render_template('cadastrarfuncionarios.html')

################CADASTRO DE MAQUINAS ######################################
@fabrica_de_roupas.route('/cadastrar/maquinas')
def cadastrar_maquinas():
    return render_template('cadastrarmaquinas.html')

################CADASTRO DE PEÇAS ######################################
@fabrica_de_roupas.route('/cadastrar/pecas')
def cadastrar_pecas():
    return render_template('cadastrarpecas.html')

##############################EXIBIR############################################
@fabrica_de_roupas.route('/exibir')
def exibir():
    return render_template('exibir.html')

@fabrica_de_roupas.route('/exibir/funcionarios')
def exibir_funcionarios():
    #apertou mostra tudo!
    return render_template('exibir.html')

@fabrica_de_roupas.route('/exibir/costureiras')
def exibir_costureiras():
    #apertou mostra tudo numa tabela dentro de exibir!
    return render_template('exibir.html')

@fabrica_de_roupas.route('/exibir/supervisoras')
def exibir_supervisoras():
    #apertou mostra tudo numa tabela dentro de exibir!
    return render_template('exibir.html')

@fabrica_de_roupas.route('/exibir/maquinas')
def exibir_maquinas():
    #apertou mostra tudo!
    return render_template('exibir.html')

@fabrica_de_roupas.route('/exibir/pecas')
def exibir_pecas():
    #apertou mostra tudo!
    return render_template('exibir.html')

@fabrica_de_roupas.route('/exibir/habilitacao')
def exibir_habilitacao():
    #apertou mostra tudo numa tabela dentro de exibir!
    return render_template('exibir.html')

@fabrica_de_roupas.route('/exibir/producao')
def exibir_producao():
    #apertou mostra tudo numa tabela dentro de exibir!
    return render_template('exibir.html')

@fabrica_de_roupas.route('/exibir/manutencao')
def exibir_manutencao():
    #apertou mostra tudo numa tabela dentro de exibir!
    return render_template('exibir.html')

########################ATUALIZAR###############################################
@fabrica_de_roupas.route('/atualizar/funcionarios')
def atualizar_funcionarios():
    return render_template('atualizarfuncionarios.html')

@fabrica_de_roupas.route('/atualizar/costureiras', methods=["GET", "POST"])
def atualizar_costureiras():
    
    if request.method == "POST":
        try:
            if request.form['issupervisora'] == "on":
                flash("Deseja Promover para supervisora?")
        except:
            pass
    else:
        pass
    return render_template('atualizarfuncionarios.html')

@fabrica_de_roupas.route('/atualizar/maquinas')
def atualizar_maquinas():
    return render_template('atualizarmaquinas.html')

@fabrica_de_roupas.route('/atualizar/pecas')
def atualizar_pecas():
    return render_template('atualizarpecas.html')

#destruir
@fabrica_de_roupas.route('/destruir')
def destruir():
    return render_template('destruir.html')

@fabrica_de_roupas.route('/destruir/funcionarios')
def destruir_funcionarios():
    return render_template('destruirfuncionarios.html')

@fabrica_de_roupas.route('/destruir/maquinas')
def destruir_maquinas():
    return render_template('destruirmaquinas.html')

@fabrica_de_roupas.route('/destruir/pecas')
def destruir_pecas():
    return render_template('destruirpecas.html')
