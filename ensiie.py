#!/usr/bin/env python3
import getpass
import requests
import argparse
import sys
import os
import time

def connect(username, password):
    # Create a session to store all the needed cookies
    s = requests.session()

    # First, let's try to connect to a sample website
    r = s.get('http://captive.apple.com', verify=False)
    if 'Success' in r.text:
        print('Vous êtes déjà connecté à Internet !')
        exit(0)
    # If there is no 'Success', it means we have arrived on the
    # captive portal instead of the website we want

    # While authentication is not done
    while (True):
        if username:
            print("Username : " + username)
        # Ask for username if not given in parameter
        if not username:
            username = input("Nom d'utilisateur : ")
        # Ask for password if not given in parameter
        if not password:
            password = getpass.getpass('Entrez votre mot de passe ENSIIE : ')
        # Authentication to ENSIIE CAS
        payload = {'user': username, 'password': password}
        j = s.post('https://opnsense.ensiie.fr:8000/api/captiveportal/access/logon/0/', data=payload, verify=False)
        response = j.json()
        if response['clientState'] == 'AUTHORIZED':
            time.sleep(10)
            break
        else:
            password = ''

    # Finally, make a test with a classic test website
    print('Vérification de la connexion')
    r = s.get('http://captive.apple.com', verify=False)
    if 'Success' in r.text:
        print('Vérification terminée : vous êtes connecté à eduspot !')

parser = argparse.ArgumentParser(description='Connect to eduspot.')
parser.add_argument('-u', '--username', help='Username of the user')
parser.add_argument('-p', '--password', help='Password of the user')
args = parser.parse_args()

try:
    connect(args.username, args.password)
except KeyboardInterrupt:
    print('\nInterrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
