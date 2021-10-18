from src import app
from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class score_table_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="cricket_tournament",user="postgres",host="localhost",password="anujagr98",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def add_batter_scores_model(self,data):
        try:
            self.cursor.execute("INSERT INTO score_table(match_id,team_id,inning,playing_as,player_id,runs,balls,fours,sixes) VALUES("+data["match_id"]+","+data["team_id"]+","+data["inning"]+",'BATTER',"+data["player_id"]+","+data["runs"]+","+data["balls"]+","+data["fours"]+","+data["sixes"]+")")
            return make_response("Score Added Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def add_bowler_scores_model(self,data):
        try:
            self.cursor.execute("INSERT INTO score_table(match_id,team_id,inning,playing_as,player_id,runs,overs,maiden_overs,wicket,wides,no_ball) VALUES("+data["match_id"]+","+data["team_id"]+","+data["inning"]+",'BOWLER',"+data["player_id"]+","+data["runs"]+","+data["overs"]+","+data["maiden_overs"]+","+data["wicket"]+","+data["wides"]+","+data["no_ball"]+")")
            return make_response("Score Added Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def list_match_score_model(self,match_id):
        try:
            self.cursor.execute("SELECT * FROM score_table WHERE match_id="+str(match_id))
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def list_team_score_model(self,match_id,inning_no):
        try:
            self.cursor.execute("SELECT * FROM score_table WHERE inning="+str(inning_no)+" AND match_id="+str(match_id))
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def list_batting_team_score_model(self,match_id,team_id):
        try:
            self.cursor.execute("SELECT * FROM score_table WHERE playing_as='BATTER' AND team_id="+str(team_id)+" AND match_id="+str(match_id))
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def list_bowling_team_score_model(self,match_id,team_id):
        try:
            self.cursor.execute("SELECT * FROM score_table WHERE playing_as='BOWLER' AND team_id="+str(team_id)+" AND match_id="+str(match_id))
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def update_batter_scores_model(self,data,score_id):
        try:
            self.cursor.execute("UPDATE score_table SET runs="+data["runs"]+", balls="+data["balls"]+", fours="+data["fours"]+", sixes="+data["sixes"]+" WHERE id="+str(score_id))
            return make_response("Score Updated Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)


    def update_bowler_scores_model(self,data,score_id):
        try:
            self.cursor.execute("UPDATE score_table SET runs="+data["runs"]+", overs="+data["overs"]+", maiden_overs="+data["maiden_overs"]+", wicket="+data["wicket"]+", wides="+data["wides"]+", no_ball="+data["no_ball"]+" WHERE id="+str(score_id))
            return make_response("Score Updated Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
         
            
    def delete_scores_model(self,score_id):
        try:
            self.cursor.execute("DELETE FROM score_table WHERE id="+str(score_id))
            return make_response("score Deleted Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)