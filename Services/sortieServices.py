import Models.sortieModel as sortieModel
import Services.userServices as userServices
from datetime import date,timedelta
current = date.today()

def toDate(pDateString):
    pDateTable = pDateString.split('-')
    print("===========Current")
    print(current)
    print("===========DateTable")
    print(pDateTable)
    return date(int(pDateTable[0]),int(pDateTable[1]),int(pDateTable[2]))
def checkDate(pDateString):
    vDate = toDate(pDateString)
    print(vDate)
    if vDate<current:
        return 407
    if vDate > current+timedelta(days=365):
        return 408
    return 203

def addSortie(pDate_Sortie, pChien_id):
    sortieModel.addSortie(pDate_Sortie, pChien_id)
    print("sortie added")
    return 203

def getSortieList(user_id):
    # On récupère le client_id grâce au service utilisateur
    client_id = userServices.getClientId(user_id)
    sortieList = sortieModel.getSortieList(client_id)
    for sortie in sortieList:
        print(sortie)
    return sortieList