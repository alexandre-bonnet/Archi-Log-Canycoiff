import Models.sortieModel as sortieModel
import Services.userServices as userServices

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