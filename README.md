# Projet Canycoiff Romane et Alex

Bienvenue dans notre salon de coiffure pour canidés !

Description du projet: 
On crée un salon de toiletteur pour chien. On peut se connecter avec son compte (ou en créer un si on n'en a pas) pour enregistrer son animal. De plus on peut l'inscrire à une sortie si l'on souhaite! 




Pour les tables, on peut gérer: 
Les clients, leurs chiens, les sorties organisées par le salon et les participations des chiens aux sorties. 
On utilise une base de données relationnelle avec des relations 1→N et N→N.

La table client contient les infos:
id (PK)
nom
téléphone

La table chien contient les infos:
id (PK)
nom
race
client_id (Fk de client)

Relation de type 1-N 

La table sortie contient les infos: 
id(PK)
date_sortie 

La table de liaison faire contient les infos: 
chien_id (FK chien)
sortie_id (FK sortie)

Relation de type N-N 

Le principe: on ajoute des clients, leus chiens, les dates de srtie et on associe les chiens aux sorties. 

La logique: 
Un client peut posséder plueirus chiens, mais un chien n'appartient qu'a un client. En revanche une sortie peut concerner plusieurs chiens et un chien peut participer a plusieurs sorties. 
