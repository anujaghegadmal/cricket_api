from src import app
from flask import request, make_response
from src.models.countries_model import countries_model
import os
import time

obj = countries_model()

@app.route("/countries/create", methods=["POST"])
def add_country():
    try:
        data = request.form
        return obj.add_country_model(data)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)

@app.route("/countries/upload_flag", methods=["POST"])
def upload_flag():
    file = request.files['file']
    current_time = str(time.time())
    time_frags = current_time.split(".")
    final_filename = time_frags[0]+time_frags[1]+os.path.splitext(file.filename)[1]
    file.save(os.path.join("C:/Users/Anuja Ghegadmal/Documents/Projects/mvc_cricket_api/src/flags",final_filename))
    return make_response({"filename":"flags/"+final_filename},200)

@app.route("/countries/read")
def list_countries():
    try:
        return obj.list_countries_model()
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
@app.route("/countries/update/<id>", methods=["POST"])
def update_country(id):
    try:
        data = request.form
        return obj.update_country_model(data,id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500) 

@app.route("/countries/delete/<id>")
def delete_country(id):
    try:
        return obj.delete_country_model(id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500) 