from src import app
from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class players_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="cricket_tournament",user="postgres",host="localhost",password="anujagr98",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def add_player_model(self,data):
        try:
            self.cursor.execute("INSERT INTO players(full_name,profile_picture,description,team_id,country_id) VALUES('"+data["full_name"]+"','"+data["profile_picture"]+"','"+data["description"]+"',"+data["team_id"]+","+data["country_id"]+")")
            return make_response("Player Added Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def list_player_model(self):
        try:
            self.cursor.execute("SELECT * FROM players")
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def read_single_player_model(self,player_id):
        try:
            self.cursor.execute("SELECT * FROM players WHERE id="+str(player_id))
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def update_player_model(self,data,player_id):
        try:
            self.cursor.execute("UPDATE players SET full_name='"+data["full_name"]+"', profile_picture='"+data["profile_picture"]+"', description='"+data["description"]+"', team_id="+data["team_id"]+", country_id="+data["country_id"]+" WHERE id="+str(player_id))
            return make_response("Player Updated Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def delete_player_model(self,player_id):
        try:
            self.cursor.execute("DELETE from players where id="+str(player_id))
            return make_response("Player Deleted Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)