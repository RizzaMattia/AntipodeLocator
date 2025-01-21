from models.conn import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    favorites = db.relationship('Favorite', backref='user', lazy=True)  # Relazione con la tabella Favorite

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User username:{self.username}>'

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    original_name = db.Column(db.String(100))
    original_lat = db.Column(db.Float, nullable=False)
    original_lon = db.Column(db.Float, nullable=False)
    antipode_name = db.Column(db.String(100))
    antipode_lat = db.Column(db.Float, nullable=False)
    antipode_lon = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Favorite {self.original_name} -> {self.antipode_name}>'
