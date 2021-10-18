from src import app, token_authenticator, token_data
from flask import request, make_response
from src.models.score_table_model import score_table_model
import os
import time

obj = score_table_model()

# Add Scores for player whose Batting
@app.route("/score_table/batter_create", methods=["POST"])
@token_authenticator()
def add_batter_scores():
    try:
        data = request.form
        return obj.add_batter_scores_model(data)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Add Scores for player whose Bowling        
@app.route("/score_table/bowler_create", methods=["POST"])
@token_authenticator()
def add_bowler_scores():
    try:
        data = request.form
        return obj.add_bowler_scores_model(data)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)

# Read Scores for Single Match
@app.route("/score_table/read/<match_id>")
def list_match_score(match_id):
    try:
        return obj.list_match_score_model(match_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Read Scores of a Match for Specific inning       
@app.route("/score_table/read_team_score/<match_id>/<inning_no>")
def list_team_score(match_id,inning_no):
    try:
        return obj.list_team_score_model(match_id,inning_no)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Read Scores of Batting Team for particular match
@app.route("/score_table/read_batting_team_score/<match_id>/<team_id>")
def list_batting_team_score(match_id,team_id):
    try:
        return obj.list_batting_team_score_model(match_id,team_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Read Scores of Bowling Team for particular match        
@app.route("/score_table/read_bowling_team_score/<match_id>/<team_id>")
def list_bowling_team_score(match_id,team_id):
    try:
        return obj.list_bowling_team_score_model(match_id,team_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Update Scores of Batting Player        
@app.route("/score_table/update_batter_scores/<score_id>", methods=["POST"])
@token_authenticator()
def update_batter_scores(score_id):
    try:
        data = request.form
        return obj.update_batter_scores_model(data,score_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500)
        
# Update Scores of Bowling Player         
@app.route("/score_table/update_bowler_scores/<score_id>", methods=["POST"])
@token_authenticator()
def update_bowler_scores(score_id):
    try:
        data = request.form
        return obj.update_bowler_scores_model(data,score_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500) 

# Delete Scores
@app.route("/score_table/delete/<score_id>")
@token_authenticator()
def delete_scores(score_id):
    try:
        return obj.delete_scores_model(score_id)
    
    except Exception as e:
        make_response({"Error":"Contact developer"},500) 