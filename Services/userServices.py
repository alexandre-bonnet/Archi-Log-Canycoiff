import Models.userModel as userModel

def userExists(pUsername):
    count = userModel.getUserCount(pUsername)
    print("count = " + count)
    if(count>0):
        return True
    return False

def usernameConditions(pUsername):
    if(len(pUsername)>12):
        return 401
    if(userExists):
        print("error ; username already exists")
        return 400
    return 200

def addUser(pUsername,pPassword):
    userModel.addUser(pUsername,pPassword)
    return 201