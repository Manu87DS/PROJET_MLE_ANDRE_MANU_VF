# MACHINE LEARNING

## Objectifs du repo

Le but de ce repo est d'entrainer quelques modèles sur un jeu de données "churn" afin de prédire si oui ou non un
client se désabonne. Ici nous avons décidé d'entrainer trois modèles:
- gradient boosting
- random forest
- logistic regression

Ces modèles seront ensuite réutilisés plus tard dans une API pour de la prédiction

## Structure du repo

- Dans le dossier data , se trouvent toutes les données nécessaires pour faire fonctionner les différents scripts de ce repo.

- Nous avons principalement deux scripts:
    - **training_models.py** dont le but est d'entrainer les trois modèles et de les sauvegarder dans le dossier **trained_models**
    
    - **testing_models.py** dont le but est de tester le score des modèles sur les jeu de données test.

## Installation nécessaire avant de lancer l'un ou l'autre des deux scripts

- se déplacer dans le dossier machine_learning
- pip install -r requirements.txt

## commande pour lancer l'entrainement des modèles

- python3 training_models.py

## commande pour lancer le testing des modèles

- python3 testing_models.py


