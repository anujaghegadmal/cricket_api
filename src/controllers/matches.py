from src import app, token_authenticator, token_data
from flask import request, make_response
from src.models.matches_model import matches_model
import os
import time

obj = matches_model()

# Add Match
@app.route("/matches/create", methods=["POST"])
@token_authenticator()
def add_match():
    try:
        data = request.form
        return obj.add_match_model(data)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)

# Read Matches
@app.route("/matches/read")
def list_match():
    try:
        return obj.list_match_model()
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
    
# Read Single Match
@app.route("/matches/read_single_match/<match_id>")
def read_single_match(match_id):
    try:
        return obj.read_single_match_model(match_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Read One Team's all Matches
@app.route("/matches/read_single_team_matches/<team_id>")
def read_single_team_matches(team_id):
    try:
        return obj.read_single_team_matches_model(team_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Update Match
@app.route("/matches/update/<match_id>", methods=["POST"])
@token_authenticator()
def update_match(match_id):
    try:
        data = request.form
        return obj.update_match_model(data,match_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)

# Delete Match
@app.route("/matches/delete/<match_id>")
@token_authenticator()
def delete_match(match_id):
    try:
        return obj.delete_match_model(match_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)