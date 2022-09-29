from .models import Schedule, User
from . import db

def add_user(_name, _address, _birthday, _email, _phone, _doc_id, _password ):
    user_var = User(name = _name, address = _address, birthday = _birthday, email = _email, phone = _phone, doc_id = _doc_id, password = _password)
    db.session.add(user_var)
    db.session.commit()

    # __tablename__ = "schedule"
    # id = db.Column(db.Integer, primary_key=True, autoincrement = True )
    # created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    # status = db.Column(db.Boolean, default = True)
    # patient_name = db.Column(db.String(150))
    # scheduled_to = db.Column(db.DateTime)
    # clinic_address = db.Column(db.String(150))
    # doctor = db.Column(db.String(150))
    # type_of_doctor = db.Column(db.String(150))
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # relation with tbl schedule 


def add_schedule(_user, _date, _clinic, _doctor, type_of_doctor, _user_id):
    schedule_var = Schedule(_user, _date, _clinic, _doctor, type_of_doctor, _user_id)
    db.session.add(schedule_var)
    db.session.commit()
    
def get_schedules(_user_id):
    schedule_var = Schedule.query.filter_by(user_id = _user_id)
    return schedule_var


#teste
# add_user('vinicios', 'rua 123', '01/01/2021', 'teste@gmail', '11993408348', '22972425812', '123456')