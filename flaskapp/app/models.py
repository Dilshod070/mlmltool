from main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True, unique=True)
    password_hash = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @staticmethod
    def get_password_hash(password):
        return password


if __name__ == '__main__':
    print(User(username='test-user'))
