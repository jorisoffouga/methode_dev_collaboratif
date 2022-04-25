# Méthode de développement collaboratif

## Projet

* Python 3.8 sur PC
* Coopération avec git sur GitHub
  * Avec Marion Tapia

Ce code qui permet de répondre au jeu suivant : https://github.com/vpoulailleau/crystal_trucks

## Algorithme

Afin d'avoir très vite un projet fonctionnel :
* pilotez un seul camion avec une double boucle sur les X et les Y, dossier : **_camion_seul_**
* pilotez ensuite un seul camion en allant au cristal le plus proche, dossier : **_camion_seul_opti_**
* pilotez ensuite plusieurs camions qui collaborent, dossier : **_camion_deplacement_opti_**

## Intégration continue
                             
Grâce à CircleCI, chaque test est joué a chaque commit et pull_request cela permet de tester notre code en continu. 

* Dans le dossier **_test_**, deux fichiers test sont present :
  * **_test_truck_** qui permet de tester la classe truck
  * **_test_roadmap_** qui permet de tester les fonctions du fichier roadmap

Pour mettre la qualimétrie de nos fichiers, un pre-commit est effectué pour formater chaque ficher que l'on souhaite
commit sur git pour verifier que la pep8 est bien respecté grace à `black`


## Exécution du programme

