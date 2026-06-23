import mysql.connector
from flask import Flask, render_template,request
import Services.userServices as userServices
#from flask_cors import CORS

app = Flask(__name__)

def getServerResponse(code):
    if(code==200):
        return "Account created !"
    elif(code ==201):
        return "Welcome to your account !"
    elif(code ==400):
        return "Username already in use"
    elif(code == 401):
        return "Username too long (12 characters max)"
    elif(code ==402):
        return "Username not found"
    elif(code ==403):
        return "Password is wrong"
    else :
        return ""

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/apropos")
def apropos():
    return render_template("apropos.html")

@app.route("/connexion",methods=["GET","POST"])
def connexion():
    userId = -1
    serverCode = 0
    serverResponse =""
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("password")
        serverCode = userServices.loginAccount(user,password)
        serverResponse = getServerResponse(serverCode)
    if(serverCode==201):
        userId = 1
        #userId = userServices.getUserId(user)
    return render_template("connexion.html",message = serverResponse,codeProfile = serverCode//100)

@app.route("/createAcount",methods=["GET","POST"])
def createAcount():
    serverCode = 0
    serverResponse = ""
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("password")
        print(user)
        print(password)
        serverCode = userServices.usernameConditions(user)
        if(serverCode==201):
            serverCode = userServices.addUser(user, password)
        serverResponse = getServerResponse(serverCode)
    return render_template("createAcount.html",message = serverResponse,codeProfile = serverCode//100)