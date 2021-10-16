from src import app
from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class venues_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="cricket_tournament",user="postgres",host="localhost",password="anujagr98",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def add_venue_model(self,data):
        try:
            self.cursor.execute("INSERT INTO venues(venue,website) VALUES('"+data["venue"]+"','"+data["website"]+"')")
            return make_response("Venue Added Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
    def list_venues_model(self):
        try:
            self.cursor.execute("SELECT * FROM venues")
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
    def update_venue_model(self,data,venue_id):
        try:
            self.cursor.execute("UPDATE venues SET venue='"+data["venue"]+"', website='"+data["website"]+"' WHERE id="+str(venue_id))
            return make_response("Venue Updated Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
    def delete_venue_model(self,venue_id):
        try:
            self.cursor.execute("DELETE FROM venues WHERE id="+str(venue_id))
            return make_response("Venue Deleted Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)