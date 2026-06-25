import Models.sortieModel as sortieModel
import Services.userServices as userServices
from datetime import date,timedelta
currentDate = date.today()

def toDate(pDateString):
    pDateTable = pDateString.split('-')
    return date(int(pDateTable[0]),int(pDateTable[1]),int(pDateTable[2]))
def checkDate(pDateString):
    vDate = toDate(pDateString)
    print(vDate)
    if vDate<currentDate:
        return 407
    if vDate > currentDate+timedelta(days=365):
        return 408
    return 203

def addSortie(pDate_Sortie, pChien_id):
    num = 204
    sortie_id = sortieModel.getSortieId(pDate_Sortie)
    if (sortie_id is None):
        sortieModel.addSortie(pDate_Sortie)
        print("sortie added")
        sortie_id = sortieModel.getSortieId(pDate_Sortie)
        num = 205
    sortieModel.addDogToSortie(pChien_id,sortie_id)
    return num

def getSortieList(user_id):
    # On récupère le client_id grâce au service utilisateur
    client_id = userServices.getClientId(user_id)
    sortieList = sortieModel.getSortieList(userServices.getClientId(user_id))
    for sortie in sortieList:
        print(sortie)
    return sortieList

def getMesChiensParSortie(user_id,Sortie_id):
    client_id = userServices.getClientId(user_id)
    return sortieModel.getDogsForSortie(client_id, Sortie_id)