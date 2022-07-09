import http

from flask import Blueprint, Response, jsonify, make_response, request

from db.db import UserDB
user_router = Blueprint('user', __name__, url_prefix='/user')
db = UserDB()


@user_router.route('')
def get():
    users = db.get_all()
    return jsonify(users)
    #return make_response(jsonify(users), http.HTTPStatus.OK, {"custom": "header"})
    #return Response(str(users))


@user_router.route('/<string:email>')
def retrieve(email):
    user = db.retrieve_by_email(email)
    return jsonify(user) #user


@user_router.route('', methods=['POST'])
def create():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    
    if not name or not email or not password :
        return Response({"Bad user model"}, http.HTTPStatus.BAD_REQUEST)
    
    new_user = db.add(name, email, password)
    return new_user, http.HTTPStatus.CREATED


@user_router.route('/<string:email>', methods=['PUT'])
def update(email):    
    name = request.json.get("name")   
    password = request.json.get("password")
    
    if not name or not email or not password :
        return Response({"Bad user model"}, http.HTTPStatus.BAD_REQUEST)
    
    user=db.update_by_email(email,name,password)    
    return jsonify(user)


@user_router.route('/<string:email>', methods=['DELETE'])
def delete(email):
    db.delete_by_email(email)
    return {}, http.HTTPStatus.NO_CONTENT
