from src import app, token_authenticator, token_data
from flask import request, make_response
from src.models.users_model import users_model
import os
import time

obj = users_model()

@app.route("/users/login", methods=["POST"])
# @cross_origin()
def login():
    try:
        data=request.form.to_dict()
        print(data)
        return obj.login_model(data)
        
    except Exception as e:
        print(e)
        return make_response({"Error":"Contact developer"},500)
    
    
@app.route("/users/create", methods=["POST"])
def add_user():
    try:
        data = request.form
        return obj.add_user_model(data)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# upload_profile_picture() used to upload profile_picture of players as well
@app.route("/users/upload_profile_picture", methods=["POST"])
@token_authenticator()
def upload_profile_picture():
    file = request.files['file']
    current_time = str(time.time())
    time_frags = current_time.split(".")
    final_filename = time_frags[0]+time_frags[1]+os.path.splitext(file.filename)[1]
    file.save(os.path.join(app.root_path+"/profile_pictures",final_filename))
    return make_response({"filename":"profile_pictures/"+final_filename},200)

@app.route("/users/read")
@token_authenticator()
def list_user():
    try:
        return obj.list_user_model()
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
    
@app.route("/users/read_single_user")
@token_authenticator()
def read_single_user():
    try:
        # print(token_data["data"]["id"])
        return obj.read_single_user_model(token_data["data"]["id"])
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
@app.route("/users/update", methods=["POST"])
@token_authenticator()
def update_user():
    try:
        data = request.form
        return obj.update_user_model(data,token_data["data"]["id"])
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)

@app.route("/users/delete")
@token_authenticator()
def delete_user():
    try:
        return obj.delete_user_model(token_data["data"]["id"])
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500) 