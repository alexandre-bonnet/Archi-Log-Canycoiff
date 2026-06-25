import Models.chienModel as chienModel
import Services.userServices as userServices

def addChien(pNomChien,race,user_id, photo):
    chienModel.addChien(pNomChien,race,userServices.getClientId(user_id),photo)
    print("dog added")
    return 202

def getDogList(user_id):
    dogList = chienModel.getDogList(userServices.getClientId(user_id))
    for dog in dogList:
        print(dog)
    return dogList


def deleteChien(user_id, dog_id):
    client_id = userServices.getClientId(user_id)
    if not chienModel.isDogOwnedByClient(dog_id, client_id):
        return False
    chienModel.removeDog(dog_id)
    return True