from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    status = db.Column(db.Boolean, default = True)
    name = db.Column(db.String(150))
    sex = db.Column(db.String(20))
    address = db.Column(db.String(150))
    birthday = db.Column(db.DateTime)
    email = db.Column(db.String(150), unique = True)
    phone = db.Column(db.String(150))
    doc_id = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    schedule_at = db.relationship('Schedule') # relation with tbl schedule 

class Schedule(db.Model):
    __tablename__ = "schedule"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True )
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    status = db.Column(db.Boolean, default = True)
    patient_name = db.Column(db.String(150))
    scheduled_to = db.Column(db.DateTime)
    clinic_address = db.Column(db.String(150))
    doctor = db.Column(db.String(150))
    type_of_doctor = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # relation with tbl schedule 

    # _patient_name, _scheduled_to, _clinic_address, _doctor, _type_of_doctor, _user_id

    # def __init__(self, id,patient_name, scheduled_to, clinic_address, doctor, type_of_doctor, user_id):
    #     self.id = id
    #     # self.created_at = created_at
    #     # self.status = status
    #     self.patient_name = patient_name
    #     self.scheduled_to = scheduled_to
    #     self.clinic_address = clinic_address
    #     self.doctor = doctor
    #     self.type_of_doctor = type_of_doctor
    #     self.user_id = user_id
    #     # self.user_id = user_id
        
class Medicos(db.Model, UserMixin):
    __tablename__ = "medicos"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(150))
    sexo = db.Column(db.String(35))
    crm = db.Column(db.String(20))
    especialidade = db.Column(db.String(100))
    endereco = db.Column(db.String(150))
    email = db.Column(db.String(150), unique = True)
    celular = db.Column(db.String(150))
    cpf = db.Column(db.String(150), unique = True)
    senha = db.Column(db.String(150))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    #schedule_at = db.relationship('Schedule') # relation with tbl schedul