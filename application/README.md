docker build . -t mon-frontend frontend
docker build . -t mon-backend backend/API
docker build . -t mon-consumer consumer

gcloud init
gcloud auth login
gcloud config set project Calculatrice_Soulairol
gcloud auth configure-docker europe-west1-docker.pkg.dev



Dans les différents sous-dossiers, des fichiers README.md sont présent pour expliquer le fonctionnement des différents fichiers (python, html, css, javaScript).

Le serveur Redis permet de stocker les résultats des calculs. Pour cela, Redis utilise des clés pour stocker chaque résultat, par exemple si on réalise un calcul qui a pour id 1 et pour résultat 20, on envoie l'id et le résultat avec
"set" dans le consumer. Pour pouvoir récupérer ce résultat dans l'api, il suffit d'utiliser "get" avec l'id du calcul (ici 1). Cela nous renvoie le résultat, c'est-à-dire 20.
