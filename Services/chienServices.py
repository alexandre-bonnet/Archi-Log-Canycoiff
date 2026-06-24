import Models.chienModel as chienModel
import userServices as userServices

def addChien(pNomChien,race,user_id):
    chienModel.addChien(pNomChien,race,userServices.getClientId(user_id))
    return 202