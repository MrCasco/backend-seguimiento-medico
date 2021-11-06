from database import db
medicfields = set(["nombre", "especialidad", "idcedula", "edad", "numerocontacto"])
patientfields = set(["nombre", "correo", "numeroseguro", "poliza"])

def validateFields(data, base):
    missingvalues=[]
    for llave, valor in data.items():
        if llave not in base:
            missingvalues.append(llave)
    return missingvalues


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
    def getPatients():
        pass

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
