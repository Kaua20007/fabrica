from main import app  # importa a aplicação do arquivo main
from flask import render_template #usado para renderizar os templates de html

@app.route('/') #define a rota - caminho da página
def  home(): # cria a função que executa a página
    return render_template('index.html') #imprime olá na tela

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


