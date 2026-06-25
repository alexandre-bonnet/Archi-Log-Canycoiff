import mysql.connector
from flask import Flask, render_template,request,redirect,url_for,session
import Services.userServices as userServices
import Services.chienServices as chienServices



#from flask_cors import CORS


app = Flask(__name__)
app.secret_key = "CanycoiffAdmin123"

def getStatus():
    if "user_id" in session:
        return "Déconnexion"
    else : 
        return "Connexion"
    return

def getServerResponse(code):
    if(code==200):
        return "Account created !"
    elif(code ==201):
        return "Welcome to your account !"
    elif(code ==202):
        return "Toutou ajouté !"
    elif(code ==400):
        return "Username already in use"
    elif(code == 401):
        return "Username too long (12 characters max)"
    elif(code ==402):
        return "Username not found"
    elif(code ==403):
        return "Password is wrong"
    elif(code ==405):
        return "Name too long (12 characters max)"
    else :
        return ""

@app.route("/")
def index():
    return render_template("index.html",statusHtml=getStatus())

@app.route("/apropos")
def apropos():
    return render_template("apropos.html",statusHtml=getStatus())

@app.route("/connexion",methods=["GET","POST"])
def connexion():
    global status
    serverCode = 0
    serverResponse =""
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("password")
        serverCode = userServices.loginAccount(user,password)
        serverResponse = getServerResponse(serverCode)
        if(serverCode==201):
            session["user_id"] = userServices.getUserId(user)
            status = "Déconnexion"
            if userServices.getClientId(session["user_id"]) is None:
                return redirect(url_for("clientInformation"))
            return redirect(url_for("espaceperso"))
        else:
            session.clear()
            status = "Connexion"
    if "user_id" in session:
        session.clear()
        status = "Connexion"
        return render_template("deconnexion.html",statusHtml=getStatus())
    return render_template("connexion.html",statusHtml=getStatus(),message = serverResponse,codeProfile = serverCode//100)


@app.route("/createAcount",methods=["GET","POST"])
def createAcount():
    serverCode = 0
    serverResponse = ""
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("password")
        serverCode = userServices.usernameConditions(user)
        if(serverCode==201):
            serverCode = userServices.addUser(user, password)
        serverResponse = getServerResponse(serverCode)
    return render_template("createAcount.html",message = serverResponse,codeProfile = serverCode//100)

@app.route("/fillClientInformation",methods=["GET","POST"])
def clientInformation():
    serverCode = 0
    serverResponse = ""
    if "user_id" in session:
        user_id = session["user_id"]
        if request.method == "POST":
            name = request.form.get("name")
            number = request.form.get("number")
            serverCode = userServices.clientConditions(name,number)
            if(serverCode==201):
                serverCode = userServices.addClient(session["user_id"],name, number)
                return redirect(url_for("espaceperso"))
        serverResponse = getServerResponse(serverCode)
        return render_template("clientInformation.html",statusHtml=getStatus(),test = userServices.getUsername(session["user_id"]),message = serverResponse,codeProfile = serverCode//100)
    return redirect(url_for("connexion"))

@app.route("/espaceperso",methods=["GET","POST"])
def espaceperso():
    if "user_id" in session:
        text = "Liste de vos chiens :"
        if request.method == "POST":
            nom = request.form.get("nom")
            race = request.form.get("race")
            chienServices.addChien(nom,race,session["user_id"])
        dogList = chienServices.getDogList(session["user_id"])
        if len(dogList)==0:
            text = "Pas encore de chien enregistré"
            dogList.append({'Nom':"-",'Race':"-"})
        client_name=userServices.getClientName(session["user_id"])
        return render_template("espaceperso.html",statusHtml=getStatus(),name=client_name,text=text,dogs = dogList)
    return redirect(url_for("connexion"))

@app.route("/add-sortie", methods=["GET", "POST"])
def add_sortie():
    if "user_id" in session:
        text = "Liste des sorties programmées :"
        if request.method == "POST":
            date_sortie = request.form.get("date_sortie")
            chien_id = request.form.get("chien_id")
            sortieService.addSortie(date_sortie, chien_id)
            
        sortieList = sortieService.getSortieList(session["user_id"])
        if len(sortieList) == 0:
            text = "Aucune sortie programmée pour le moment"
            dogList = userServices.chienServices.getDogList(session["user_id"]) 
        return render_template("sortie.html", text=text, sorties=sortieList, chiens=dogList)
    return redirect(url_for("connexion"))