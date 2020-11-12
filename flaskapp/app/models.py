from app import db, login
from flask_login import UserMixin


class User(UserMixin, db.Model):

    __tablename__ = 'planner_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True, unique=True)
    password_hash = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @staticmethod
    def get_password_hash(password):
        pwd_hash = 0
        for char in password:
            pwd_hash = pwd_hash * 10 + ord(char)
        return pwd_hash

    def set_password(self, password):
        self.password_hash = self.get_password_hash(password)

    def check_password(self, password):
        return self.password_hash == self.get_password_hash(password)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
