import mysql.connector
from flask import Flask, render_template,request
#from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/connexion",methods=["GET","POST"])
def connexion():
    return render_template("appli.html")
  
