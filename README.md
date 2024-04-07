# JARI App

## Installation
lancer le script `install.sh` pour installer les dépendances et lancer le serveur de développement

```bash
./install.sh
```


## Commandes utiles
Lancer serveur de développement
```bash
python3 manage.py runserver
```

Faire les migrations
```bash
python3 manage.py makemigrations app
```

Exectuer les migrations
```bash
python3 manage.py migrate
```

Ajouter des données de test
```bash
python3 manage.py insert_test_data
```