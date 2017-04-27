# Script de connexion automatique à ensiie (et eduspot) - ENSIIE #

Script de connexion rapide au portail captif de eduspot en envoyant
des requêtes GET et POST aux bonnes urls. Ce script gère uniquement la
connexion dans le cadre de l'ENSIIE.

## Dépendances ##

* (UPDATE 27/04 pour le nouveau portail) ~~[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)~~
* [requests](http://docs.python-requests.org/en/master/)

## Utilisation ##

```
    $ ensiie.py [-h] [-u USERNAME] [-p PASSWORD]
```

Si le nom d'utilisateur ou le mot de passe n'est pas donné au script,
il sera demandé à l'exécution.

* * *

# Connection script to 'ensiie' (and 'eduspot') wireless hotspot @ ENSIIE #

Connection script to log faster to ~~eduspot~~ ensiie captive portal
with GET and POST requests to the right urls. Actually the script
works only at ENSIIE (engineering computer science school).

## Dependencies ##

* (UPDATE 27/04 for the new portal) ~~[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)~~
* [requests](http://docs.python-requests.org/en/master/)

## Usage ##

```
    $ ensiie.py [-h] [-u USERNAME] [-p PASSWORD]
```

If no username or password is given to the script, it will be asked
during runtime.
