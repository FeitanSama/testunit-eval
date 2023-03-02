# API CRUD + UNITTEST

## Requirements

A la racine du projet executez la commande suivante pour installer les libraires nécessaire au bon fonctionnement du projet.

```
pip install -r requirements.txt
```

Les librairies sont les suivantes : 

- unittest (tests unitaires)
- requests (faire des requêtes sur pour les tests)
- uvicorn (lancer un serveur local)
- fastapi (créer les routes api ainsi que les actions CRUD)
- motor (traitement asynchrone pour la base mongodb)
- bson (decodage des trames pour mongodb (json))
- pydantic (annotations des types des champs de la base)

## Lancement du projet

Toujours à la racine du projet executez la commande suivante pour lancer le serveur locale et préremplir la base de données avec le jeu de données cars_data.json

```
python app/main.py
```

## Vérification du lancement du projet

Se rendre sur l'adresse suivante dans votre navigateur

```
http://127.0.0.1:8000/
```

# Execution des Tests

Lancer en local le fichier **test_api.py** situé dans le dossier test\unit pour lancer les tests sur la base de données et l'API
