from app import fabrica_de_roupas
from flask import render_template
from flask import request
from flask import flash
import pymysql
conexao =pymysql.connect(host='localhost',user='root',password='root',db='mjcosturafeliz')
c =conexao.cursor()
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

    if request.method == 'POST':
        m = request.form['matricula']
        n = request.form['nome']
        v =request.form['valor']
        c =conexao.cursor()
        comando = """insert into funcionario(matricula,nome) values (%s,%s);"""
        try:
            c.execute(comando,(m,n))
        except:
            print("Matricula existente")
            result = "Matricula existente"
            return render_template('cadastrarfuncionarios.html',result = result)
        comando = """insert into costureira(valor_minimo,matricula_func) values (%s,%s);"""
        c.execute(comando,(v,m))
        
        conexao.commit()
    return render_template('cadastrarfuncionarios.html',result = 'Cadastrado')

@fabrica_de_roupas.route('/cadastrar/supervisora', methods=["GET", "POST"])
def cadastrar_supervisora():

    if request.method == 'POST':
        m = request.form['matricula']
        n = request.form['nome']
        c =conexao.cursor()
        comando = """insert into funcionario(matricula,nome) values (%s,%s);"""
        try:
            c.execute(comando,(m,n))
            comando = """insert into supervisora(matricula_func) values (%s);"""
            c.execute(comando,(m))
            conexao.commit()
            print("sucesso")

        except:
            print("Matricula existente")
            result = "Matricula existente"
            return render_template('cadastrarfuncionarios.html',result = result)
        
    return render_template('cadastrarfuncionarios.html',result = 'Cadastrado')

################CADASTRO DE MAQUINAS ######################################
@fabrica_de_roupas.route('/cadastrar/maquinas', methods=["GET", "POST"])
def cadastrar_maquinas():
    
    if request.method == 'POST':
        codigo = request.form['codigo']
        local = request.form['local']
        fab =request.form['fabricante']
        corte = request.form['descricao']
        c =conexao.cursor()
        comando = """insert into maquina(codigo, localizacao, fabricante) values (%s,%s,%s);"""
        c.execute(comando,(codigo,local,fab))
        comando = """insert into capacitacao(codigo_maquina, descricao) values (%s,%s);"""
        c.execute(comando,(codigo,corte))
        conexao.commit()
        print("sucesso")
        return render_template('index.html')

    return render_template('cadastrarmaquinas.html')

################CADASTRO DE PEÇAS ######################################
@fabrica_de_roupas.route('/cadastrar/pecas', methods=["GET", "POST"])
def cadastrar_pecas():

    if request.method == 'POST':
        #verificar se existe a costureira
        mat_cost = request.form['mat_cost']
        mat_cost = int(mat_cost)
        c =conexao.cursor()
        comando = """Select * from costureira where matricula_func = {};""".format(mat_cost)
        #arrumar um jeito de amostrar para na tela
        c.execute(comando)
        countrow = c.execute(comando)
        if countrow == 1:
            modelo = request.form['modelo']
            descricao = request.form['descricao']
        
            comando = """insert into peca(modelo,descricao,matricula_costureira) values (%s,%s,%s);"""
            c.execute(comando,(modelo,descricao,mat_cost))
            conexao.commit()
            print("sucesso")
            return render_template('index.html')
        conexao.commit()
        print("matricula invalida")
        result ="matricula invalida"
        return render_template('cadastrarpecas.html',result=result)
    return render_template('cadastrarpecas.html')

##############################EXIBIR############################################
@fabrica_de_roupas.route('/exibir')
def exibir():
    return render_template('exibir.html')

@fabrica_de_roupas.route('/exibir/funcionarios')
def exibir_funcionarios():
    #apertou mostra tudo!
    comando ='''select * from funcionario'''
    c.execute(comando)
    results= c.fetchall()
    return render_template('exibirfuncionarios.html',results=results)

@fabrica_de_roupas.route('/exibir/costureiras')
def exibir_costureiras():
    #apertou mostra tudo numa tabela dentro de exibir!
    comando ='''select nome, matricula 
    from funcionario f,  costureira  c 
    where f.matricula = c.matricula_func;'''

    c.execute(comando)
    results= c.fetchall()
    return render_template('exibirfuncionarios.html',results=results)

@fabrica_de_roupas.route('/exibir/supervisoras')
def exibir_supervisoras():
    #apertou mostra tudo numa tabela dentro de exibir!
    comando ='''select nome, matricula 
    from funcionario f,  supervisora  s 
    where f.matricula = s.matricula_func;'''
    
    c.execute(comando)
    results= c.fetchall()
    return render_template('exibirfuncionarios.html',results=results)

@fabrica_de_roupas.route('/exibir/maquinas')
def exibir_maquinas():
    #apertou mostra tudo!
    comando ='''select codigo,localizacao,fabricante from maquina;'''
    c.execute(comando)
    results= c.fetchall()
    return render_template('exibirfuncionarios.html',results=results)

@fabrica_de_roupas.route('/exibir/pecas')
def exibir_pecas():
    #apertou mostra tudo!
    comando ='''select modelo,descricao, matricula_costureira from peca;'''
    c.execute(comando)
    results= c.fetchall()
    return render_template('exibirfuncionarios.html',results=results)

@fabrica_de_roupas.route('/exibir/habilitacao')
def exibir_habilitacao():
    #apertou mostra tudo numa tabela dentro de exibir!
    comando ='''select * from habilitacao'''
    c.execute(comando)
    results= c.fetchall()
    return render_template('exibirfuncionarios.html',results=results)

@fabrica_de_roupas.route('/exibir/capacitacao')
def exibir_producao():
    #apertou mostra tudo numa tabela dentro de exibir!
    comando ='''select codigo as codigo_maquina , localizacao, data_inicio,data_termino, nome as nome_do_responsavel
    from maquina, manutencao, funcionario
    where maquina.codigo = manutencao.codigo_maquina and manutencao.matricula_func = funcionario.matricula;'''
    c.execute(comando)
    results= c.fetchall()
    return render_template('exibirfuncionarios.html',results=results)

@fabrica_de_roupas.route('/exibir/manutencao')
def exibir_manutencao():
    #apertou mostra tudo numa tabela dentro de exibir!
    comando ='''select * from manutencao'''
    c.execute(comando)
    results= c.fetchall()
    return render_template('exibirfuncionarios.html',results=results)

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

@fabrica_de_roupas.route('/atualizar/supervisora', methods=["GET", "POST"])
def atualizar_supervisora():
    
    if request.method == "POST":
        pass
    else:
        pass
    return render_template('atualizarfuncionarios.html')

@fabrica_de_roupas.route('/atualizar/maquinas', methods=["GET", "POST"])
def atualizar_maquinas():
    if request.method == "POST":
        pass
    else:
        pass
    return render_template('atualizarmaquinas.html')

@fabrica_de_roupas.route('/atualizar/pecas', methods=["GET", "POST"])
def atualizar_pecas():
    if request.method == "POST":
        pass
    else:
        pass
    return render_template('atualizarpecas.html')

#destruir
@fabrica_de_roupas.route('/destruir')
def destruir():
    return render_template('destruir.html')

@fabrica_de_roupas.route('/destruir/funcionarios', methods=["GET", "POST"])
def destruir_funcionarios():
    if request.method == "POST":
        pass
    else:
        pass
    return render_template('destruirfuncionarios.html')

@fabrica_de_roupas.route('/destruir/maquinas', methods=["GET", "POST"])
def destruir_maquinas():
    if request.method == "POST":
        pass
    else:
        pass
    return render_template('destruirmaquinas.html', methods=["GET", "POST"])

@fabrica_de_roupas.route('/destruir/pecas', methods=["GET", "POST"])
def destruir_pecas():
    if request.method == "POST":
        pass
    else:
        pass
    return render_template('destruirpecas.html')
