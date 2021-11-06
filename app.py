from flask import Flask, redirect, url_for, request
from login import login_logic
from crud_operations import Patient, Medic, Prescription
app = Flask(__name__)

@app.route('/patients-of-medic/')
def medics_patients():
    return Medic.getPatients(request.args['correo'])


@app.route('/prescriptions-of-patient/')
def prescriptions_of_patient():
    return Patient.getPrescriptions(request.args['correo'])


@app.route('/medic/', methods = ['POST', 'GET', 'DELETE'])
def medic():
    if request.method == 'POST':
        mail = request.form['correo']
        medic = Medic.getMedic(mail)
        if medic:
            return 'Medico ya registrado'
        response = Medic.insertMedic(dict(request.form))
        if not response:
            return 'Medico guardado correctamente'
        print(response)
        return 'Falta: '+', '.join(response)
    elif request.method == 'GET':
        medic = Medic.getMedic(request.args.get('correo'))
        if not medic:
            return 'No existe el medico'
        return medic
    elif request.method == 'DELETE':
        mail = request.args['correo']
        return Medic.deleteMedic(mail)


@app.route('/patient/', methods = ['POST', 'GET', 'DELETE'])
def patient():
    if request.method == 'POST':
        mail = request.form['correo']
        medic = Patient.getPatient(mail)
        if medic:
            return 'Paciente ya registrado'
        response = Patient.insertPatient(dict(request.form))
        if not response:
            return 'Paciente guardado correctamente'
        print(response)
        return 'Falta:'+', '.join(response)
    elif request.method == 'GET':
        medic = Patient.getPatient(request.args.get('correo'))
        if not medic:
            return 'No existe el paciente'
        return medic
    elif request.method == 'DELETE':
        mail = request.args['correo']
        return Patient.deletePatient(mail)


@app.route('/prescription/', methods = ['POST', 'GET', 'DELETE'])
def prescriptions():
    if request.method == 'POST':
        response = Prescription.insertPrescription(dict(request.form))
        if not response:
            return 'Receta creada correctamente'
        print(response)
        return 'Falta:'+', '.join(response)
    elif request.method == 'GET':
        pres = Prescription.getPrescription(request.args.get('id'))
        if not pres:
            return 'No existe la receta'
        return pres
    elif request.method == 'DELETE':
        id = request.args['id']
        return Prescription.deletePrescription(id)


@app.route('/login/<tipo>', methods = ['POST'])
def login(tipo):
    login_logic(tipo)


if __name__ == '__main__':
   app.run(debug = True)
