from database import db

def validateFields(data):
    missingvalues = []
    for llave, valor in data.items():
        if valor == '':
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
                    response = validateFields(data)
                    if not response:
                        db.collection('recetas').document().set(data)
                        db.collection('medicos').document(medic).collection('pacientes').document(patient).set(data)
                        return []
                    else:
                        return response
                else:
                    return ['Paciente no existe']
            else:
                return ['Medico no existe']
        except Exception as e:
            print(e)
            return [e]

    def deletePrescription(id):
        try:
            db.collection('recetas').document(id).delete()
        except Exception as e:
            print(e)
            return 'Error en borrar receta'
        return 'Recata borrada correctamente'

class Patient:
    def updatePatient(mail, data):
        print(mail, data)
        try:
            db.collection('pacientes').document(mail).update(data)
            return 'Paciente actualizado correctamente'
        except Exception as e:
            print(e)
            return str(e)


    def getPrescriptions(mail):
        docs = db.collection('recetas').where('paciente', '==', mail).stream()
        pres = []
        for doc in docs:
            pres.append(doc.to_dict())
        return str(pres)

    def getPatient(mail):
        doc = db.collection('pacientes').document(mail).get()
        if doc.exists:
            return doc.to_dict()
        return False

    def insertPatient(data):
        try:
            response = validateFields(data)
            if not response:
                mail = data['correo']
                data.pop('correo')
                db.collection('pacientes').document(mail).set(data)
                return []
            else:
                return response
        except Exception as e:
            print(e)
            return [e]

    def deletePatient(mail):
        try:
            db.collection('pacientes').document(mail).delete()
        except Exception as e:
            return e
        return 'Baja de paciente correcta'

class Medic:
    def getPatients(mail):
        docs = db.collection('medicos').document(mail).collection('pacientes').stream()
        return ', '.join([doc.id for doc in docs])

    def getMedic(mail):
        doc = db.collection('medicos').document(mail).get()
        if doc.exists:
            return doc.to_dict()
        return False

    def insertMedic(data):
        try:
            response = validateFields(data)
            if not response:
                mail = data['correo']
                data.pop('correo')
                db.collection('medicos').document(mail).set(data)
                return []
            else:
                return response
        except Exception as e:
            print(e)
            return [e]

    def deleteMedic(mail):
        try:
            db.collection('medicos').document(mail).delete()
        except Exception as e:
            return e
        return 'Borrado correctamente'
