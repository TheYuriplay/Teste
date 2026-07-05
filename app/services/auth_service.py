from passlib.hash import bcrypt
from app.database.connection import get_session
from app.models.user import User


def create_user(username: str, password: str, full_name: str = None, email: str = None):
    session = get_session()
    try:
        hashed = bcrypt.hash(password)
        user = User(username=username, password_hash=hashed, full_name=full_name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    finally:
        session.close()


def authenticate(username: str, password: str):
    session = get_session()
    try:
        user = session.query(User).filter(User.username == username).one_or_none()
        if not user or not user.password_hash:
            return None
        if bcrypt.verify(password, user.password_hash):
            return user
        return None
    finally:
        session.close()


def ensure_default_admin():
    session = get_session()
    try:
        admin = session.query(User).filter(User.username == "admin").one_or_none()
        if admin is None:
            hashed = bcrypt.hash("admin")
            admin = User(username="admin", password_hash=hashed, full_name="Administrator", is_active=True)
            session.add(admin)
            session.commit()
    finally:
        session.close()
