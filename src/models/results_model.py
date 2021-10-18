from src import app
from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class results_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="cricket_tournament",user="postgres",host="localhost",password="anujagr98",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def add_result_model(self,data):
        try:
            self.cursor.execute("INSERT INTO results(team_id,total_match_count,win_count,lose_count,points) VALUES("+data["team_id"]+","+data["total_match_count"]+","+data["win_count"]+","+data["lose_count"]+","+data["points"]+")")
            return make_response("Result Added Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def list_results_model(self):
        try:
            self.cursor.execute("SELECT * FROM results")
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def update_result_model(self,data,result_id):
        try:
            self.cursor.execute("UPDATE results SET team_id="+data["team_id"]+", total_match_count="+data["total_match_count"]+", win_count="+data["win_count"]+", lose_count="+data["lose_count"]+", points="+data["points"]+" WHERE id="+str(result_id))
            return make_response("Result Updated Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def delete_result_model(self,result_id):
        try:
            self.cursor.execute("DELETE FROM results WHERE id="+str(result_id))
            return make_response("Result Deleted Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)