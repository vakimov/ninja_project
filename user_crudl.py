from werkzeug.security import generate_password_hash, check_password_hash
from models import db_session, User


def generate_pass_hash(password):
    pass_hash = generate_password_hash(password, salt_length=100)
    return pass_hash[20:len(pass_hash)]


def create_user(first_name, email, password, last_name=None):
    pass_hash = generate_pass_hash(str(password))
    new_user = User(first_name, email, pass_hash, last_name)
    db_session.add(new_user)
    db_session.commit()
    return "Пользователь успешно создан"


def read_user(first_name=None, email=None, last_name=None, id=None):
    u = User
    if id is not None:
        return u.query.filter(User.id == id).first()
    elif email is not None:
        return u.query.filter(User.email == email).first()
    elif first_name and last_name is not None:
        return u.query.filter(User.first_name == first_name, User.last_name == last_name).first()
    else:
        return 'Такого пользователя не существует'


def delete_user(first_name=None, email=None, last_name=None, id=None):
    del_user = read_user(first_name, email, last_name, id)
    db_session.delete(del_user)
    db_session.commit()
    return 'Пользователь удалён'


