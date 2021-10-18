from src import app, token_authenticator, token_data
from flask import request, make_response
from src.models.venues_model import venues_model
import os
import time

obj = venues_model()

# Add Venue
@app.route("/venues/create", methods=["POST"])
@token_authenticator()
def add_venue():
    try:
        data = request.form
        return obj.add_venue_model(data)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)

# Read Venue
@app.route("/venues/read")
def list_venues():
    try:
        return obj.list_venues_model()
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
    
# Update Venue    
@app.route("/venues/update/<venue_id>", methods=["POST"])
@token_authenticator()
def update_venue(venue_id):
    try:
        data = request.form
        return obj.update_venue_model(data,venue_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500) 

# Delete Venue
@app.route("/venues/delete/<venue_id>")
@token_authenticator()
def delete_venue(venue_id):
    try:
        return obj.delete_venue_model(venue_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)