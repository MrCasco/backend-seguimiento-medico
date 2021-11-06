from flask import Flask, redirect, url_for, request
from login import login_logic
from crud_operations import Patient, Medic
app = Flask(__name__)

@app.route('/medic/', methods = ['POST', 'GET', 'DELETE'])
def medic():
    if request.method == 'POST':
        mail = request.form['correo']
        medic = Medic.getMedic(mail)
        if medic:
            return 'Medico ya registrado'
        elif Medic.insertMedic(dict(request.form)):
            return 'Medico guardado correctamente'
        return 'Hubo un problema'
    elif request.method == 'GET':
        medic = Medic.getMedic(request.args.get('correo'))
        if not medic:
            return 'No existe el medico'
        return medic
    elif request.method == 'DELETE':
        mail = request.form['correo']
        return Medic.deleteMedic(mail)

@app.route('/patient/', methods = ['POST', 'GET', 'DELETE'])
def patient():
    if request.method == 'POST':
        mail = request.form['correo']
        medic = Patient.getPatient(mail)
        if medic:
            return 'Paciente ya registrado'
        elif Patient.insertPatient(dict(request.form)):
            return 'Paciente guardado correctamente'
        return 'Hubo un problema'
    elif request.method == 'GET':
        medic = Patient.getPatient(request.args.get('correo'))
        if not medic:
            return 'No existe el paciente'
        return medic
    elif request.method == 'DELETE':
        mail = request.form['correo']
        return Patient.deletePatient(mail)

@app.route('/login/<tipo>', methods = ['POST'])
def login(tipo):
    login_logic(tipo)

if __name__ == '__main__':
   app.run(debug = True)
