from database import db

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
