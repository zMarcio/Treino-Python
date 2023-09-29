from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient

app = Flask(__name__)

uri = ''

client = MongoClient(uri)

db = client.StudyLoginTest

collection = db.StudyLoginTest

@app.route('/', methods=['GET','POST'])
def login_page():

    if request.method == 'POST':
        email_digitado = request.form['usuario']
        senha_digitada = request.form['senha']
        
        usuario = collection.find_one({"$or": [{'email': email_digitado}, {'first': email_digitado}]})

        if usuario:
        
            if senha_digitada == usuario['password']:
                return f'Login bem-sucedido, senhor(a): {usuario["first"]}'
        
        else:
            return f'Usuário não encontrado.'
        
    return render_template("login.html")
                
    #     for usuario in dados:
    #         if (usuario['email'] == email_digitado or usuario['first'] == email_digitado) and usuario['password'] == senha_digitada:
    #             return f'Login bem-sucedido, senhor(a): {usuario["first"]}'
        
    #     return "Credenciais inválidas. Tente novamente."
    

if __name__ == '__main__':
    app.run(debug=True)
