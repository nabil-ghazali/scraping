# Importer les bibliothèques nécessaires
import requests
import json
import pandas as pd


# URL de l'API Google Books
url = 'https://www.googleapis.com/books/v1/volumes'

parameters = {}

def search_parameters () ->dict:
    """
    Demande à l'utilisateur les mots-clés de recherche pour le paramètre obligatoire 'q'.
    Renvoie le dictionnaire de paramètres mis à jour.
    """
    while True:
        q_params = input("Vous pouvez spécifier des mots clés pour effectuer des recherches :")
        match q_params :
            case "":
                q_params= input("Veuillez spécifier des mots clés spéciaux pour effectuer des recherches :")
            case _: 
                parameters["q"]=q_params
                return parameters
    
def printType_parameters () -> dict:

    print( " Veuillez choisir quel contenu vous souhaitez entre les propositions suivantes : ")
    params = input (" books / magazines or all : ")
    while True:
        match params.lower().strip():  # pour éviter les problèmes de casse
            case "books":
                parameters['printType'] = 'books'
                return parameters
            case "magazines":
                parameters['printType'] = 'magazines'
                return parameters
            case "all":
                parameters['printType'] = 'all'
                return parameters
            case _:
                params = input (" books / magazines or all : ")           

def filter_parameters () ->dict:
    """
    Permet à l'utilisateur de filtrer les résultats selon différents critères.
    Renvoie le dictionnaire de paramètres mis à jour.
    """

    print( " Veuillez choisir la visualisation des résultats dans les propositions suivantes, selon les diffèrents 'filter'  : ")

    filters = input(" partial : limite les résultats aux volumes dont au moins une partie du texte est disponible en aperçu. \n full : limite les résultats aux volumes où tout le texte est visible. \n free-ebooks : limite les résultats aux livres numériques sans frais sur Google. \n paid-ebooks : limite les résultats aux e-books Google avec un prix d'achat. \n ebooks : limite les résultats aux livres numériques Google, payants ou gratuits.\n ") 

    while True:
        match filters.lower().strip():  # pour éviter les problèmes de casse
            case "partial":
                parameters['filter'] = 'partial'
                return parameters
            case "full":
                parameters['filter'] = 'full'
                return parameters
            case "free-ebooks":
                parameters['filter'] = 'free-ebooks'
                return parameters
            case "paid-ebooks":
                parameters['filter'] = 'paid-ebooks'
                return parameters
            case "ebooks":
                parameters['filter'] = 'ebooks'
                return parameters
            case _:
                filters = input("filter=partial : limite les résultats aux volumes dont au moins une partie du texte est disponible en aperçu \n.filter=full : limite les résultats aux volumes où tout le texte est visible \n.filter=free-ebooks : limite les résultats aux livres numériques sans frais sur Google \n.filter=paid-ebooks : limite les résultats aux e-books Google avec un prix d'achat.filter=ebooks : limite les résultats aux livres numériques Google, payants ou gratuits.") 
            
def numberResult_parameters() -> dict:

    """
    Demande à l'utilisateur un nombre de résultats (entre 1 et 40).
    Ne sort de la boucle que si une entrée valide est saisie.
    """
    while True:
        user_input = input("Veuillez choisir le nombre de résultats à renvoyer (entre 1 et 40) : ")

        if user_input.strip() == "":
            print("Ce champ est obligatoire. Veuillez entrer un nombre.")
            continue

        if not user_input.isdigit():
            print("Entrée invalide. Veuillez entrer un nombre entier.")
            continue

        number_result = int(user_input)
        if 1 <= number_result <= 40:
            parameters['maxResults'] = number_result
            return parameters
        else:
            print("Veuillez entrer un nombre compris entre 1 et 40.")

def order_parameters() -> dict:
    """
    Permet à l'utilisateur de choisir l'ordre des résultats (relevance ou newest).
    Renvoie le dictionnaire de paramètres mis à jour.
    """
    print( " Choisissez parmis les propositions suivantes :")

    while True:
        user_input = input(" Vous pouvez modifier l'ordre en définissant le paramètre orderBy sur l'une des valeurs suivantes: .\n relevance : renvoie les résultats par ordre de pertinence des termes de recherche (valeur par défaut). \n newest : renvoie les résultats dans l'ordre de publication, du plus récent au moins récent. \n ").strip().lower()

        if user_input.strip() == "":
            print("Ce champ est obligatoire")
                

        elif user_input  not in ["relevance", "newest"]:
            print("Veuillez entrer relevance ou newest")
            
        else :
            parameters['orderBy'] = user_input
            return parameters

def get_data_API( url= 'https://www.googleapis.com/books/v1/volumes'):
    search_parameters()
    printType_parameters()
    filter_parameters()
    numberResult_parameters()
    order_parameters()
    # Requêter l'API Google Books
    response = requests.get(url, params=parameters)

    # Vérifier le code de statut de la réponse
    if response.status_code == 200:
        print("Requête réussie :", response.status_code)
    else:
        print("Erreur :", response.status_code)

    # Vérification de l'URL s'il a été correctement codée en imprimant l'URL :
    print(response.url)

    # # Affichage du contenu de la réponse du serveur
    # print(response.text)
    # print(response.content)
    # Récupérer le coeur de la réponse
    data_books_raw = response.json()
    return data_books_raw

