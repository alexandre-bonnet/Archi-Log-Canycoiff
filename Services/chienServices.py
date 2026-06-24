import Models.chienModel as chienModel
import Services.userServices as userServices

def addChien(pNomChien,race,user_id):
    chienModel.addChien(pNomChien,race,userServices.getClientId(user_id))
    print("dog added")
    return 202

def getDogList(user_id):
    dogList = chienModel.getDogList(userServices.getClientId(user_id))
    for dog in dogList:
        print(dog)
    return dogList