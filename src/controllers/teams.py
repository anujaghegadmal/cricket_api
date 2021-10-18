from src import app, token_authenticator, token_data
from flask import request, make_response
from src.models.teams_model import teams_model
import os
import time

obj = teams_model()

# Add Team
@app.route("/teams/create", methods=["POST"])
@token_authenticator()
def add_team():
    try:
        data = request.form
        return obj.add_team_model(data)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Upload Team logo
@app.route("/teams/upload_team_logo", methods=["POST"])
@token_authenticator()
def upload_team_logo():
    file = request.files['file']
    current_time = str(time.time())
    time_frags = current_time.split(".")
    final_filename = time_frags[0]+time_frags[1]+os.path.splitext(file.filename)[1]
    file.save(os.path.join(app.root_path+"/team_logo",final_filename))
    return make_response({"filename":"team_logo/"+final_filename},200)

# Read Teams
@app.route("/teams/read")
def list_teams():
    try:
        return obj.list_teams_model()
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Read Single Team
@app.route("/teams/read_single_team/<team_id>")
def read_single_team(team_id):
    try:
        return obj.read_single_team_model(team_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Update Team
@app.route("/teams/update/<team_id>", methods=["POST"])
@token_authenticator()
def update_team(team_id):
    try:
        data = request.form
        return obj.update_team_model(data,team_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500) 

# Delete Team
@app.route("/teams/delete/<team_id>")
@token_authenticator()
def delete_team(team_id):
    try:
        return obj.delete_team_model(team_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)