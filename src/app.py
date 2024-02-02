"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)




@app.route('/members', methods=['GET'])
def members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }


    return jsonify(response_body), 200



@app.route('/member/<int:member_id>', methods=['GET'])
def member(member_id):

    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"msg": "this member dosn't exist"})
    
    return jsonify(member), 200
    


@app.route('/member', methods=['POST'])
def add_member():
    
    request_body = request.json
    new_member = {
        "first_name": request_body["first_name"],
        "last_name": jackson_family.last_name,
        "age": request_body["age"],
        "lucky_numbers": request_body["lucky_numbers"]
        }
    data = jackson_family.add_member(new_member)
    
    if data is None:
        return jsonify({"message": "Member added successfully"}), 201
    else:
        return jsonify(data), 400  # Cambiado a código de estado 201 para indicar creación exitosa
    
        
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.delete_member(member_id)
    if member is None:
        return jsonify({"msj": "the user dosn't exist"}), 404

    return jsonify(member), 200


    
    
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
