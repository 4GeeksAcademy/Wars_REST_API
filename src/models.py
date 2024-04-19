from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    gravedad = db.Column(db.String(80), unique=False, nullable=False)
    poblacion = db.Column(db.String(80), unique=False, nullable=False)
    habitable = db.Column(db.String(80), unique=False, nullable=False)

   
    tipo = db.Column(db.String(250))
    clima = db.Column(db.String(250))
    
    

    def __repr__(self):
        return '<Planeta %r>' % self.planeta

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "gravedad": self.gravedad,
            "poblacion": self.poblacion,
            "habitable": self.habitable,
            "tipo": self.tipo,
            "clima": self.clima,
            # do not serialize the password, its a security breach
        }