from src import app, token_authenticator, token_data
from flask import request, make_response
from src.models.countries_model import countries_model
import os
import time

obj = countries_model()

# Add Country
@app.route("/countries/create", methods=["POST"])
@token_authenticator()
def add_country():
    try:
        data = request.form
        return obj.add_country_model(data)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)

# Upload Country Flag
@app.route("/countries/upload_flag", methods=["POST"])
@token_authenticator()
def upload_flag():
    file = request.files['file']
    current_time = str(time.time())
    time_frags = current_time.split(".")
    final_filename = time_frags[0]+time_frags[1]+os.path.splitext(file.filename)[1]
    file.save(os.path.join(app.root_path+"/flags",final_filename))
    return make_response({"filename":"flags/"+final_filename},200)

# Read Countries
@app.route("/countries/read")
def list_countries():
    try:
        return obj.list_countries_model()
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
      
# Update Country
@app.route("/countries/update/<country_id>", methods=["POST"])
@token_authenticator()
def update_country(country_id):
    try:
        data = request.form
        return obj.update_country_model(data,country_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500) 

# Delete Country
@app.route("/countries/delete/<country_id>")
@token_authenticator()
def delete_country(country_id):
    try:
        return obj.delete_country_model(country_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500) 