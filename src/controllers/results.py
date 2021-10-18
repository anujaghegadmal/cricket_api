from src import app, token_authenticator, token_data
from flask import request, make_response
from src.models.results_model import results_model
import os
import time

obj = results_model()

# Add Result
@app.route("/results/create", methods=["POST"])
@token_authenticator()
def add_result():
    try:
        data = request.form
        return obj.add_result_model(data)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)

# Read Results
@app.route("/results/read")
def list_results():
    try:
        return obj.list_results_model()
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Update Result        
@app.route("/results/update/<result_id>", methods=["POST"])
@token_authenticator()
def update_result(result_id):
    try:
        data = request.form
        return obj.update_result_model(data,result_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500) 

# Delete Result
@app.route("/results/delete/<result_id>")
@token_authenticator()
def delete_result(result_id):
    try:
        return obj.delete_result_model(result_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500) 