from flask import Flask, redirect, url_for, request
from database import db
app = Flask(__name__)

def getMedic(mail):
    doc = db.collection('medicos').document(mail).get()
    if doc.exists:
        return doc.to_dict()
    return False

def insertMedic(data):
    try:
        mail = data['correo']
        data.pop('correo')
        db.collection('medicos').document(mail).set(data)
    except Exception as e:
        print(e)
        return False
    return True

def deleteMedic(mail):
    try:
        db.collection('medicos').document(mail).delete()
    except Exception as e:
        return e
    return 'Borrado correctamente'

@app.route('/medic/', methods = ['POST', 'GET', 'DELETE'])
def medic():
    if request.method == 'POST':
        mail = request.form['correo']
        medic = getMedic(mail)
        if medic:
            return 'Medico ya registrado'
        elif insertMedic(dict(request.form)):
            return 'Medico guardado correctamente'
        return 'Hubo un problema'
    elif request.method == 'GET':
        medic = getMedic(request.args.get('correo'))
        if not medic:
            return 'No existe el medico'
        return medic
    elif request.method == 'DELETE':
        mail = request.form['correo']
        return deleteMedic(mail)

@app.route('/patient/', methods = ['POST', 'GET', 'DELETE'])
def patient():
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
      user = request.form.get('correo')
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
