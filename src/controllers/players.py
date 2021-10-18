from src import app, token_authenticator, token_data
from flask import request, make_response
from src.models.players_model import players_model
import os
import time

obj = players_model()

# Add Player
@app.route("/players/create", methods=["POST"])
@token_authenticator()
def add_player():
    try:
        data = request.form
        return obj.add_player_model(data)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)

# Read Players
@app.route("/players/read")
def list_player():
    try:
        return obj.list_player_model()
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
    
# Read Single Player
@app.route("/players/read_single_player/<player_id>")
def read_single_player(player_id):
    try:
        return obj.read_single_player_model(player_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Update Player        
@app.route("/players/update/<player_id>", methods=["POST"])
@token_authenticator()
def update_player(player_id):
    try:
        data = request.form
        return obj.update_player_model(data,player_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)

# Delete Player
@app.route("/players/delete/<player_id>")
@token_authenticator()
def delete_player(player_id):
    try:
        return obj.delete_player_model(player_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)