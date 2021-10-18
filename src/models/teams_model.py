from src import app
from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class teams_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="cricket_tournament",user="postgres",host="localhost",password="anujagr98",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def add_team_model(self,data):
        try:
            self.cursor.execute("INSERT INTO teams(team,team_logo,country_id) VALUES('"+data["team"]+"','"+data["team_logo"]+"',"+data["country_id"]+")")
            return make_response("Team Added Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def list_teams_model(self):
        try:
            self.cursor.execute("SELECT * FROM teams")
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def read_single_team_model(self,team_id):
        try:
            self.cursor.execute("SELECT * FROM teams WHERE id="+str(team_id))
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def update_team_model(self,data,team_id):
        try:
            self.cursor.execute("UPDATE teams SET team='"+data["team"]+"', team_logo='"+data["team_logo"]+"', country_id="+data["country_id"]+" WHERE id="+str(team_id))
            return make_response("Team Updated Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def delete_team_model(self,team_id):
        try:
            self.cursor.execute("DELETE FROM teams WHERE id="+str(team_id))
            return make_response("Team Deleted Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)