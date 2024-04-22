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

#aqui empiezo a añadir codigo---------------------------
class Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    gravedad = db.Column(db.String(80), unique=False, nullable=False)
    poblacion = db.Column(db.String(80), unique=False, nullable=False)
    habitable = db.Column(db.String(80), unique=False, nullable=False)
    tipo = db.Column(db.String(250), unique=False, nullable=False)
    clima = db.Column(db.String(250), unique=False, nullable=False)
    
    

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
    

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    raza = db.Column(db.String(80), unique=False, nullable=False)
    altura = db.Column(db.String(80), unique=False, nullable=False)
    peso = db.Column(db.String(80), unique=False, nullable=False)
    sexo = db.Column(db.String(80), unique=False, nullable=False)
    color_pelo = db.Column(db.String(80), unique=False, nullable=False)
    
    

    def __repr__(self):
        return '<People %r>' % self.people

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "raza": self.raza,
            "altura": self.altura,
            "peso": self.peso,
            "sexo": self.sexo,
            "color_pelo": self.color_pelo,
            # do not serialize the password, its a security breach
        }
    

class Vehiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    tipo = db.Column(db.String(80), unique=False, nullable=False)
    velocidad = db.Column(db.String(80), unique=False, nullable=False)
    peso = db.Column(db.String(80), unique=False, nullable=False)
    tripulacion = db.Column(db.String(80), unique=False, nullable=False)
    armamento = db.Column(db.String(80), unique=False, nullable=False)
    
    

    def __repr__(self):
        return '<Vehiculos %r>' % self.vehiculos

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.raza,
            "velocidad": self.velocidad,
            "peso": self.peso,
            "tripulacion": self.tripulacion,
            "armamento": self.armamento,
            # do not serialize the password, its a security breach
        }

    #   aqui empieza los favoritos------------------------


class FavoritosPlaneta(db.Model):
    __tablename__ = "favoritos_planeta"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    planeta_id = db.Column(db.Integer, db.ForeignKey('planeta.id'))


    def __repr__(self):
        return '<FavoritosPlaneta %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planeta": self.planeta_id_id,
        } 


class FavoritosPeople(db.Model):
    __tablename__ = "favoritos_people"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))


    def __repr__(self):
        return '<FavoritosPeople %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people": self.people_id_id,
        } 


class FavoritosVehiculos(db.Model):
    __tablename__ = "favoritos_vehiculos"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    vehiculos_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'))


    def __repr__(self):
        return '<FavoritosVehiculos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehiculos_id": self.vehiculos_id_id,
        }   


