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

    def __init__(self, id, text, created_time=None):
        self.title = title
        self.text = text
