from database import db

doc_ref = db.collection('medicos').document('sss')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})
