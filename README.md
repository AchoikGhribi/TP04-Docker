TP04: Docker Containerization and Big Data Deployment
University of Eloued - Big Data Analytics
Nom : GHRIBI ACHOIK
Groupe : 1

Réponses aux questions
1. C'est quoi Docker et pourquoi on l'utilise en Data Science ?

En fait, Docker c'est un outil qui permet de mettre une application et tous ses composants (Python, les bibliothèques comme pandas, etc.) dans un seul "paquet" qu'on appelle une image.
Pour la Data Science, c'est très pratique parce que ça règle le problème du "ça marche chez moi mais pas chez toi". Ça isole aussi les projets, donc on n'a plus de conflits entre les versions des bibliothèques. Et c'est facile à partager avec l'équipe ou à déployer sur un serveur.

2. La différence entre une Image et un Conteneur ?

Pour faire simple :

L'Image : C'est comme une recette de cuisine ou un modèle statique. On la construit avec un Dockerfile, elle ne consomme pas de mémoire, et elle ne change pas.

Le Conteneur : C'est le plat cuisiné. C'est une instance active de l'image. Quand on le lance, il consomme du CPU et de la RAM, et on peut interagir avec.

3. À quoi servent FROM, WORKDIR, COPY, RUN et CMD ?

Ce sont les instructions qu'on écrit dans le Dockerfile :

FROM : C'est l'image de base qu'on utilise (par exemple python:3.11-slim).

WORKDIR : Ça permet de définir le dossier de travail dans le conteneur (comme /app).

COPY : Ça copie les fichiers de notre ordinateur vers le conteneur.

RUN : Ça exécute des commandes pendant la construction de l'image (comme pip install).

CMD : C'est la commande qui se lance automatiquement quand le conteneur démarre (comme python app.py).

4. Quel problème Docker Compose résout-il ?

Docker Compose est très utile quand on a plusieurs conteneurs à gérer. Au lieu de taper de longues commandes docker run à chaque fois (avec les ports, les réseaux, etc.), on met tout dans un fichier compose.yaml. Comme ça, avec une seule commande docker compose up, tout se lance automatiquement.

5. Comparaison entre docker run et docker compose up ?

docker run : C'est manuel. On gère un seul conteneur à la fois avec une longue ligne de commande. C'est difficile à reproduire exactement.

docker compose up : C'est automatique. Tout est écrit dans le fichier YAML, donc c'est facile à partager, à reproduire, et ça gère les réseaux et volumes tout seul.

6. Comment ajouter un service de base de données ?

On ajoute simplement un nouveau service dans le fichier compose.yaml. Par exemple pour PostgreSQL :

```
yaml
services:
  data-analysis:
    build: .
    depends_on:
      - database
    environment:
      - DB_HOST=database
      - DB_PORT=5432

  database:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: tp04db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```


Structure du projet :
```
TP04_Docker/
├── app.py
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── README.md
├── data/
│   └── train_small.csv
└── screenshots/
    ├── docker_ps.png
    ├── docker_compose.png
    ├── localhost_8001.png
    └── docker_hub.png
```
Lien Docker Hub : https://hub.docker.com/r/achoik203q/tp04-analysis