from src import app
from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class matches_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="cricket_tournament",user="postgres",host="localhost",password="anujagr98",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def add_match_model(self,data):
        try:
            self.cursor.execute("INSERT INTO matches(venue_id,team_1,team_2) VALUES("+data["venue_id"]+","+data["team_1"]+","+data["team_2"]+")")
            return make_response("Match Added Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
    def list_match_model(self):
        try:
            self.cursor.execute("SELECT * FROM matches")
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
    def read_single_match_model(self,match_id):
        try:
            self.cursor.execute("SELECT * FROM matches WHERE id="+str(match_id))
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
    def update_match_model(self,data,match_id):
        try:
            self.cursor.execute("UPDATE matches SET winner='"+data["winner"]+"', looser='"+data["looser"]+"', man_of_the_match='"+data["man_of_the_match"]+"', bowler_of_the_match="+data["bowler_of_the_match"]+", best_fielder="+data["best_fielder"]+" WHERE id="+str(match_id))
            return make_response("Match Updated Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
    def delete_match_model(self,match_id):
        try:
            self.cursor.execute("DELETE from matches where id="+str(match_id))
            return make_response("Match Deleted Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)