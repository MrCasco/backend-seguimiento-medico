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

def getPatient(mail):
    doc = db.collection('pacientes').document(mail).get()
    if doc.exists:
        return doc.to_dict()
    return False

def insertPatient(data):
    try:
        mail = data['correo']
        data.pop('correo')
        db.collection('pacientes').document(mail).set(data)
    except Exception as e:
        print(e)
        return False
    return True

def deletePatient(mail):
    try:
        db.collection('pacientes').document(mail).delete()
    except Exception as e:
        return e
    return 'Baja de paciente correcta'

@app.route('/patient/', methods = ['POST', 'GET', 'DELETE'])
def patient():
    if request.method == 'POST':
        mail = request.form['correo']
        medic = getPatient(mail)
        if medic:
            return 'Medico ya registrado'
        elif insertMedic(dict(request.form)):
            return 'Medico guardado correctamente'
        return 'Hubo un problema'
    elif request.method == 'GET':
        medic = getPatient(request.args.get('correo'))
        if not medic:
            return 'No existe el medico'
        return medic
    elif request.method == 'DELETE':
        mail = request.form['correo']
        return deletePatient(mail)

@app.route('/login/<tipo>', methods = ['POST'])
def login(tipo):
    mail = request.form['correo']
    password = request.form['password']
    if tipo == 'medico':
        medic = getMedic(mail)
        if not medic:
            return 'Correo incorrecto'
        if password != medic['contraseña']:
            return 'Contraseña incorrecta'
        return 'Login correcto!'
    patient = getPatient(mail)
    if not patient:
        return 'Correo incorrecto'
    if password != patient['contraseña']:
        return 'Contraseña incorrecta'
    return 'Login correcto!'

if __name__ == '__main__':
   app.run(debug = True)
