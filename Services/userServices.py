import Models.userModel as userModel

def userExists(pUsername):
    count = userModel.getUserCount(pUsername)
    if(count>0):
        return True
    return False

def usernameConditions(pUsername):
    if(len(pUsername)>12):
        return 401
    if(userExists(pUsername)):
        print("error ; username already exists")
        return 400
    return 201

def clientConditions(pName,pNumber):
    if(len(pName)>20):
        return 405
    return 201

def addUser(pUsername,pPassword):
    userModel.addUser(pUsername,pPassword)
    return 200

def getUserId(pUsername):
    return userModel.getUserId(pUsername)

def getUsername(user_id):
    return userModel.getUsername(user_id)

def getClientId(user_id):
    return userModel.getClientId(user_id)

def addClient(user_id,pName,pNumber):
    userModel.addClient(user_id,pName,pNumber)
    return 200

def loginAccount(pUsername,pPassword):
    if(userExists(pUsername)):
        if(userModel.passwordValidity(pUsername,pPassword)):
            return 201
        else :
            return 403
    else :
        return 402