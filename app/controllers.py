from .models import User
from . import db

def add_user(_name, _address, _birthday, _email, _phone, _doc_id, _password ):
    user_var = User(name = _name, address = _address, birthday = _birthday, email = _email, phone = _phone, doc_id = _doc_id, password = _password)
    db.session.add(user_var)
    db.session.commit()


#teste
# add_user('vinicios', 'rua 123', '01/01/2021', 'teste@gmail', '11993408348', '22972425812', '123456')