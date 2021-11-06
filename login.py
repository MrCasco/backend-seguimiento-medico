from crud_operations import Medic, Patient

def login_logic():
    mail = request.form['correo']
    password = request.form['password']
    if tipo == 'medico':
        medic = Medic.getMedic(mail)
        if not medic:
            return 'Correo incorrecto'
        if password != medic['contraseña']:
            return 'Contraseña incorrecta'
        return 'Login correcto!'
    patient = Patient.getPatient(mail)
    if not patient:
        return 'Correo incorrecto'
    if password != patient['contraseña']:
        return 'Contraseña incorrecta'
    return 'Login correcto!'
