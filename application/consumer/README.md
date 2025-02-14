Dans ce dossier, il y a un fichier python consumer.py qui permet de réaliser le calcul demandé sur la page web. En effet, dans un premier temps, on se connecte à un serveur Redis pour pouvoir par la suite
envoyé le résultat du calcul dedans. Ensuite, il y a une fonction calcul() qui prend en paramètre 2 nombres et un opérateur pour effectuer le calcul demandé. Suivant l'opérateur, la fonction retourne le résultat de l'opération.
Après cela, on initialise la connexion à RabbitMQ et on créer la file d'attente. Enfin, la fonction réception permet de récupérer le tuple envoyé par l'api dans RabbitMQ grâce à l'utilisation de canaux de communication.
Cette fonction décode le tuple reçu pour récupérer les différentes valeurs dans des variables. Elle appelle ensuite la fonction calcul pour exécuter le calcul avec les données extraites et envoi le résultat
sur le serveur Redis pour pouvoir le récupérer dans l'api.
