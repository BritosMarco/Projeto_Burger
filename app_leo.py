from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import classes

app = Flask(__name__)


#Configuracoes de acceso ao banco de dados
user='xqtbbsoy'
password='BIjm6OQGv7Q-F0JC5LouLKvC8TtDhMsT'
host='kesavan.db.elephantsql.com'
database='xqtbbsoy'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key ="pepe pepe pepe"

#Intanciando objeto da Classe SQLAlchemy 
db = SQLAlchemy(app)

#-----------------------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/favicon.ico")
def principal():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/menu', methods=['GET','POST'])
def menu():
    produtos = classes.Produtos.produtos_read_all()
    return render_template('menu.html', produtos=produtos)

@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    novo_cadastro = None
    existe = None
    cnome = None
    csobrenome = None
    if (request.method == 'POST'):
        form = request.form
        email = form['email']
        existe_email= classes.Clientes.consultar_email(email)
        if existe_email == True:
            existe = "Seu email encontra-se cadastrado em nosso sistema"
            novo_cadastro = True
            return render_template('cadastro.html', existe=existe, novo_cadastro = novo_cadastro, email=email)
        novo_cliente = classes.Clientes(nome=form['nome'], sobrenome=form['sobrenome'], email=form['email'], telefone=form['telefone'], usuario=form['usuario'], senha=form['senha'])
        db.session.add(novo_cliente)
        db.session.commit()
        id_cliente = classes.Clientes.consultar_id(email)
        if id_cliente == None:
            existe = "Ocorreu um erro, por favor intente se cadastrar novamento"
            novo_cadastro = True
            return render_template('cadastro.html', existe=existe, novo_cadastro = novo_cadastro)
        novo_endereco = classes.Enderecos(id_cliente=id_cliente, cep=form['cep'], numero=form['numero'], rua=form['rua'], complemento=form['complemento'])
        db.session.add(novo_endereco)
        db.session.commit()
        novo_forma_pagamento = classes.Forma_pagamento(id_cliente=id_cliente, numero_cartao=form['numero_cartao'], cpf=form['cpf'], nome=form['nome_cartao'], validade_mes=form['mes_vencimento'], validade_ano=form['ano_vencimento'])
        db.session.add(novo_forma_pagamento)
        db.session.commit()
        novo_cadastro = True
        cnome= form['nome']
        csobrenome = form['sobrenome']
    return render_template('cadastro.html', novo_cadastro=novo_cadastro, cnome=cnome, csobrenome=csobrenome)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if (__name__ == '__main__'):
    app.run(debug=True)
