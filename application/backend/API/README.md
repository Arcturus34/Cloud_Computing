On retrouve ici le fichier de l'api. Ici, il a été choisi d'utiliser une api Flask en python pour faciliter l'utilisation de Redis et RabbitMQ. Dans un premier temps, on initialise Flask et Redis pour pouvoir
les utiliser par la suite. Ensuite, on créé une route /api/calculate. Cette route permet dans un premier temps de récupérer les données d'un calcul envoyé par le fichier javaScript du frontend. On récupère
ces différentes valeurs pour pouvoir construire le tuple à envoyé sur le serveur RabbitMQ. Ensuite, on génère un id pour pouvoir retrouver le résultat du calcul sur le serveur Redis. On se connecte ensuite à RabbitMQ
et on envoie le tuple crée avec les différentes informations nécessaire pour la réalisation du calcul à RabbitMQ.
Une deuxième route est également présente. Cette route permet de récupérer le résultat qui se trouve sur le serveur Redis. Le résultat est récupéré avec r.get en spécifiant l'id du calcul précédemment effecuté.
