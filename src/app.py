"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Planeta,People

from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


#endpoints-------------------------------------


@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/user/<int:user_id>', methods=['GET'])
def ghandle_user_favorito():

    response_body = {
        "msg": "Hello, this is your GET /user/favorito response "
    }

    return jsonify(response_body), 200




   #endpoint de people--------------------------------

@app.route('/people', methods=['GET'])
def handle_people():

    response_body = {
        "msg": "Hello, this is your GET /people response "
    }

    return jsonify(response_body), 200

 #endpoint para 1 solo personaje------------------

@app.route('/people/<int:people_id>', methods=['GET'])
def get_one_people(people_id):
  #  print(people_id)

    people_query = People.query.filter_by(id=people_id).first()
    print(people_query)
   
    if people_query is None:
        return jsonify({"msg":"people info no found"}),404

    response_body = {
        "msg": "ok",
        "result": people_query.serialize()
     }

    return jsonify(response_body), 200

 #endpoint para crear una personaje ------------------------------------------------


@app.route('/people/', methods=['POST'])
def create_people():
    body= request.json
    
    people_query = People.query.filter_by(nombre=body["nombre"]).first()
    if people_query is None:


        new_people = People(nombre=body["nombre"], raza=body["raza"],altura=body["altura"],peso=body["peso"],sexo=body["sexo"],color_pelo=body["color_pelo"])
        db.session.add(new_people)
        db.session.commit()
        return jsonify({"msg":"people created"}), 200
    else:
        return jsonify({"msg":"people exist"}), 400
    
    #endpoint para borrar al personaje--------------------------------------

@app.route("/people/<int:people_id>", methods=["DELETE"])
def delete_people():
    body=request.json

    people_query = People.query.filter_by(nombre=body["nombre"]).first()
    if people_query is None:

    
        me = People(id=body["id"], nombre=body["nombre"],raza=body["raza"],altura=body["altura"],peso=body["peso"],sexo=body["sexp"],color_pelo=body["color_pelo"])
        db.session.delete(me)
        db.session.commit()
        return jsonify({"msg":"people delete"}), 200
    else:
        return jsonify({"msg":"people exist"}), 400

#---------------------------------------------------------
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    jackson_family.delete_member(member_id)
    
    return jsonify({"msg":"El miembro ha sido borrado"}),200

def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"done":True}
#------------------------------------------------------------




#endpoints de planetas------------------------------------
@app.route('/planeta', methods=['GET'])
def ghandle_planeta():

    response_body = {
        "msg": "Hello, this is your GET /planeta response "
    }

    return jsonify(response_body), 200

@app.route('/planeta/<int:planeta_id>', methods=['GET'])
def get_one_planeta():

    response_body = {
        "msg": "Hello, this is your GET /planeta/favorito response "
    }

    return jsonify(response_body), 200


# endpoints de vehiculos---------------------

@app.route('/vehiculos', methods=['GET'])
def ghandle_vehiculos():

    response_body = {
        "msg": "Hello, this is your GET /vehiculos response "
    }

    return jsonify(response_body), 200


@app.route('/vehiculos/<int:people_id>', methods=['GET'])
def get_one_vehiculos():

    response_body = {
        "msg": "Hello, this is your GET /vehiculos/favorito response "
    }

    return jsonify(response_body), 200


#este endpoint es para verificar el registro de un usuario esta en la lista

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user_query = User.query.filter_by(email=email).first()
    print(user_query)
    
    if user_query is None:
        return jsonify({"msg": "Email no ta"}),

    if email != user_query.email or password != user_query.password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.

@app.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    user_query = User.query.filter_by(email=current_user).first()
    print(user_query)

    return jsonify({"result":"ok"}), 200




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)




#voy por la ninea 115
#modigicar 119 y añadir correctamente quien es el que se borra