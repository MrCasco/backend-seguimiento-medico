from database import db
medicfields = set(["nombre", "especialidad", "idcedula", "edad", "numerocontacto"])
patientfields = set(["nombre", "correo", "numeroseguro", "poliza"])

def validateFields(data, base):
    missingvalues=[]
    for llave, valor in data.items():
        if llave not in base:
            missingvalues.append(llave)

    return missingvalues            
    

class Patient:
    def getPatient(mail):
        doc = db.collection('pacientes').document(mail).get()
        if doc.exists:
            return doc.to_dict()
        return False

    def insertPatient(data):
        try:
            validateFields(data, patientfields)
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
            validateFields(data, medicfields)
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
