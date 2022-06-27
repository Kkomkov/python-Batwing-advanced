
from app import app
from helpers.file import get_users, write_users
from flask import render_template, request, redirect
import logging, sys


def filter_users(users,parameters):
    if (parameters):
        parameter_email = parameters.get("email")
        parameter_first_name = parameters.get("first_name")
        parameter_last_name = parameters.get("last_name")
        parameter_work_area= parameters.get("work_area")
        
        logging.debug(f'email: {parameter_email}')
        logging.debug(f'first_name: {parameter_first_name}')
        logging.debug(f'last_name: {parameter_last_name}')
        logging.debug(f'work_area: {parameter_work_area}')
        
        if(parameter_email) :
            users = filter(lambda element : element['email'] == parameter_email,users)
        
        if(parameter_first_name) :
            users = filter(lambda element : element['first_name']== parameter_first_name,users)
        
        if(parameter_last_name) :
            users = filter(lambda element : element['last_name'] == parameter_last_name,users)
        
        if(parameter_work_area) :
            users = filter(lambda element : element['work_area'] == parameter_work_area,users)
        
        logging.debug(f'user: {users}')
    return users


@app.route("/")
def main():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    users = get_users()
    users = filter_users(users,request.args )
        
    return render_template("index.html", users=users)


@app.route("/user-add")
def user_add():
    return render_template("user-add.html")


@app.route("/users", methods=["POST"])
def save_user():
    users = get_users()
    id = 1
    if len(users) > 0:
        id = len(users) + 1
    user = {
        "id": id,
        "email": request.form.get("email"),
        "first_name": request.form.get("first_name"),
        "last_name": request.form.get("last_name"),
        "work_area": request.form.get("working_area")
    }
    users.append(user)
    write_users(users)
    return redirect("/")


@app.route("/user-edit/<int:id>")
def edit(id):
    users = get_users()
    for user in users:
        if user["id"] == id:
            return render_template("user-add.html", user=user)
    return redirect("/")


@app.route("/users/<int:id>", methods=["POST"])
def update(id):
    users = get_users()
    for user in users:
        if user["id"] == id:
            user["email"] = request.form.get("email")
            user["first_name"] = request.form.get("first_name")
            user["last_name"] = request.form.get("last_name")
            user["work_area"] = request.form.get("working_area")
    write_users(users)
    return redirect("/")


@app.route("/users/delete/<int:id>")
def delete(id):
    users = get_users()
    del users[id - 1]
    write_users(users)
    return redirect("/")
