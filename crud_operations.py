from database import db

class Prescription:
    def getPrescription(id):
        doc = db.collection('pacientes').document(id).get()
        if doc.exists:
            return doc.to_dict()
        return False

    def insertPrescription(data):
        try:
            patient = data['paciente']
            medic = data['medico']
            if Medic.getMedic(medic):
                if Patient.getPatient(patient):
                    db.collection('recetas').document().set(data)
                else:
                    return 'Paciente no valido'
            else:
                return 'Medico no valido'
        except Exception as e:
            print(e)
            return False
        return True

    def deletePrescription(id):
        try:
            db.collection('recetas').document(id).delete()
        except Exception as e:
            return e
        return 'Baja de paciente correcta'

class Patient:
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

class Medic:
    def getPatients():

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
