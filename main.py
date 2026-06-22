import mysql.connector
from flask import Flask, render_template,request
import userServices
#from flask_cors import CORS

app = Flask(__name__)

def getServerResponse(code):
    if(code==200):
        return "created"
    elif(code ==400):
        return "username already in use"
    else :
        return ""


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/connexion",methods=["GET"])
def connexion():
    return render_template("connexion.html")

@app.route("/createAcount",methods=["GET","POST"])
def createAcount():
    serverCode = 0
    serverResponse = ""
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("password")
        print(user)
        print(password)
        serverCode = userServices.userValid(user, password)
        if(serverCode==200):
            userServices.addUser(user, password)
        serverResponse = getServerResponse(serverCode)
    return render_template("createAcount.html",message = serverResponse,codeProfile = serverCode//100)