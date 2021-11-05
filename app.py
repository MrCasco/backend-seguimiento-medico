from flask import Flask, redirect, url_for, request
from database import db
app = Flask(__name__)

@app.route('/medic/', methods = ['POST', 'GET', 'DELETE'])
def medic():
    if request.method == 'POST':
       print(dict(request.form))
       return request.form.get('nombre')
    elif request.method == 'GET':
        print(request.args.get('id'))
        return 'medico existente'
    elif request.method == 'DELETE':
        print('eliminar medico')
        return 'eliminar medico'

@app.route('/login', methods = ['POST'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
