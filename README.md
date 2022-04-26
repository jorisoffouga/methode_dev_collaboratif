# Méthode de développement collaboratif

## Projet

* Python 3.8 sur PC
* Coopération avec git sur GitHub
  * Avec Marion Tapia

Ce code qui permet de répondre au jeu suivant : https://github.com/vpoulailleau/crystal_trucks

## Algorithme

Afin d'avoir très vite un projet fonctionnel :
* pilotez un seul camion avec une double boucle sur les X et les Y, dossier : [**_camion_seul_**](./camion_seul)
* pilotez ensuite un seul camion en allant au cristal le plus proche, dossier : [**_camion_seul_opti_**](./camion_seul_opti)
* pilotez ensuite plusieurs camions qui collaborent, dossier : [**_camion_deplacement_opti_**](./camion_deplacement_opti)

## Intégration continue
                             
Grâce à CircleCI, chaque test est joué a chaque commit et pull_request cela permet de tester notre code en continu. 

* Dans le dossier [**_test_**](./test), deux fichiers test sont present :
  * **_[test_truck.py](./test/test_truck.py)_** qui permet de tester la classe truck
  * **_[test_roadmap.py](./test/test_roadmap.py)_** qui permet de tester les fonctions du fichier roadmap

Pour mettre la qualimétrie de nos fichiers, un pre-commit est effectué pour formater chaque ficher que l'on souhaite
commit sur git pour verifier que la pep8 est bien respecté grace à `black`.


## Exécution du programme

Faire un git clone du repo

`git clone https://github.com/dylan6440/methode_dev_collaboratif.git`

Avoir python3.8 (ou supérieure) pour crée un environement virtuel.

`python3.8 -m venv <nom_environement_virtuel>`

Activé environnement virtuel.

`<nom_environement_virtuel>/Scripts/activate` 

Si vous etes sur windows il faut mettre la ligne suivante:

`<nom_environement_virtuel>/Scripts/Activate.ps1` 

Une fois votre environnement actif, installer les librairies recommandé.

`pip install -r requierements.txt`

Maintenant vous pouvez exécuter le main avec comme argument <numero_map> <fichier_ecriture.txt>

`python main.py <numero_map> <fichier_ecriture.txt>`

Une fois le fichier texte ecrit avec la map choisit, on peux lancer le jeux.

`cd crystal_trucks`

`python viewer.py -i ../<fichier_ecriture.txt>`

La fenêtre de jeux s'ouvre !
