from src import app
from flask import request, make_response
from src.models.users_model import users_model
import os
import time

obj = users_model()

@app.route("/users/create", methods=["POST"])
def add_user():
    try:
        data = request.form
        return obj.add_user_model(data)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)

@app.route("/users/upload_profile_picture", methods=["POST"])
def upload_profile_picture():
    file = request.files['file']
    current_time = str(time.time())
    time_frags = current_time.split(".")
    final_filename = time_frags[0]+time_frags[1]+os.path.splitext(file.filename)[1]
    file.save(os.path.join("C:/Users/Anuja Ghegadmal/Documents/Projects/mvc_cricket_api/src/profile_pictures",final_filename))
    return make_response({"filename":"profile_pictures/"+final_filename},200)

@app.route("/users/read")
def list_user():
    try:
        return obj.list_user_model()
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
    
@app.route("/users/read_single_user/<id>")
def read_single_user(id):
    try:
        return obj.read_single_user_model(id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
@app.route("/users/update/<id>", methods=["POST"]) 
def update_user(id):
    try:
        data = request.form
        return obj.update_user_model(data,id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)

@app.route("/users/delete/<id>")
def delete_user(id):
    try:
        return obj.delete_user_model(id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500) 