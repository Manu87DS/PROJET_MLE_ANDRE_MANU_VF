# But du repo 

L'objectif de ce repo est de créer une API qui permet d'interroger les modèles créés lors de la phase de machine learnig.

Dans un premier temps nous avons créé le code de l'API puis dans un second temps nous avons créé un dockerfile
afin de pouvoir lancer l'API dans un container.

# Instructions pour builder et pousser l'image (en supposant qu'on est loggé)

- se déplacer dans le dossier fastapi
- docker image build . -t andre1994/fastapi_churn
- docker image push andre1994/fastapi_churn

# Instruction pour lancer le conteneur

- docker container run -d -p 8000:8000 --name andre andre1994/fastapi_churn