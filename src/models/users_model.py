from src import app
from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor
import jwt
import datetime

class users_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="cricket_tournament",user="postgres",host="localhost",password="anujagr98",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def login_model(self,data):
        try:
            self.cursor.execute("SELECT * FROM users WHERE email='"+data["email"]+"' AND password='"+data["password"]+"'")
            fd = self.cursor.fetchall()
            if len(fd)>0:
                # print(fd)
                token = jwt.encode({"data":fd,"exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=500)},"EncryptionKey")
                return make_response({"payload":token},200)
            else:
                return make_response({"Error":"Please check EMAIL or PASSWORD"},403)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def add_user_model(self,data):
        try:
            self.cursor.execute("INSERT INTO users(full_name,profile_picture,email,password,phone_no) VALUES('"+data["full_name"]+"','"+data["profile_picture"]+"','"+data["email"]+"','"+data["password"]+"',"+data["phone_no"]+")")
            return make_response("User Added Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
    def list_user_model(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
    def read_single_user_model(self,id):
        try:
            self.cursor.execute("SELECT * FROM users WHERE id="+str(id))
            fd = self.cursor.fetchall()
            return make_response({"payload":fd},200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
    def update_user_model(self,data,id):
        try:
            self.cursor.execute("UPDATE users SET full_name='"+data["full_name"]+"', profile_picture='"+data["profile_picture"]+"', email='"+data["email"]+"', password='"+data["password"]+"', phone_no="+data["phone_no"]+" WHERE id="+str(id))
            return make_response("User Updated Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)
            
    def delete_user_model(self,id):
        try:
            self.cursor.execute("DELETE from users where id="+str(id))
            return make_response("User Deleted Successfully",200)
        
        except Exception as e:
            make_response({"Error":str(e)},500)