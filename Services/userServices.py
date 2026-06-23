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
        print("userExists = true")
    print("===============")
    if(userExists(pUsername)):
        print("error ; username already exists")
        return 400
    return 200

def addUser(pUsername,pPassword):
    userModel.addUser(pUsername,pPassword)
    return 201

def loginAccount(pUsername,pPassword):
    if(userExists(pUsername)):
        if(userModel.passwordValidity(pUsername,pPassword)):
            return 201
        else :
            return 403
    else :
        return 402