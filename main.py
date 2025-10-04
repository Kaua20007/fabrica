from flask import Flask # importa a biblioteca

app = Flask(__name__) # cria a aplicação
 

from templates.routes import * # importa tudo que é do arquivo routes

if __name__ == '__main__':
    app.run(debug=True)