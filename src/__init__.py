from flask import Flask,request,make_response,jsonify
app=Flask('src')
import jwt,re,json
from functools import wraps

token_data={}
def token_authenticator(expected_role=""):
    def inner_decorator(fun):
        @wraps(fun)
        def inner(*args,**kwargs):
            try:
                authorization = request.headers.get("authorization")
                if re.match("^Bearer *([^ ]+) *$",authorization,flags=0):
                    token = authorization.split(" ")[1]
                    decoded = jwt.decode(token,"EncryptionKey",algorithms="HS256")
                    token_data["data"] = decoded["data"][0]
                    # print(token_data["data"])
                    return fun(*args,**kwargs)
                else:
                    return make_response({"Error":"Invalid Token"})
            except Exception as e:
                return make_response({"Error":str(e)},500)
        return inner
    return inner_decorator

from src.controllers import *