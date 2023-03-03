from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(120), nullable=True)
    first_name = db.Column(db.String(32), nullable=True)
    last_name = db.Column(db.String(32), nullable=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))

    def __repr__(self):
        return f'<User: {self.username}>'
    
    def __str__(self) -> str:
        return f'<User: {self.email}|{self.username}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)
    

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(32), nullable=True)
    model = db.Column(db.String(32), nullable=True)
    year = db.Column(db.String(10), nullable=True)
    color = db.Column(db.String(32), nullable=True)
    price = db.Column(db.Float(), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

    def __repr__(self):
        return f'<Car: {self.year} {self.model} {self.make}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()