from src import app
from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class countries_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="cricket_tournament",user="postgres",host="localhost",password="anujagr98",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def add_country_model(self,data):
        try:
            self.cursor.execute("INSERT INTO countries(country,flag) VALUES('"+data["country"]+"','"+data["flag"]+"')")
            return make_response("Country Added Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def list_countries_model(self):
        try:
            self.cursor.execute("SELECT * FROM countries")
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def update_country_model(self,data,country_id):
        try:
            self.cursor.execute("UPDATE countries SET country='"+data["country"]+"', flag='"+data["flag"]+"' WHERE id="+str(country_id))
            return make_response("Country Updated Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
            
    def delete_country_model(self,country_id):
        try:
            self.cursor.execute("DELETE FROM countries WHERE id="+str(country_id))
            return make_response("Country Deleted Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)