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
    """
    Demande à l'utilisateur de choisir un type de contenu à rechercher (books, magazines, ou all).
    Met à jour le dictionnaire global 'parameters' avec la clé 'printType'.

    Returns:
        dict: Le dictionnaire des paramètres mis à jour avec le type de contenu choisi.
    """
    print( " Veuillez choisir quel contenu vous souhaitez entre les propositions suivantes : ")
    params = input (" books / magazines or all : \n ")
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

    print( " Veuillez choisir la visualisation des résultats dans les propositions suivantes, selon les diffèrents 'filter'  : \n")

    filters = input(" partial : limite les résultats aux volumes dont au moins une partie du texte est disponible en aperçu. \n \n full : limite les résultats aux volumes où tout le texte est visible. \n \n free-ebooks : limite les résultats aux livres numériques sans frais sur Google. \n \n paid-ebooks : limite les résultats aux e-books Google avec un prix d'achat. \n \n ebooks : limite les résultats aux livres numériques Google, payants ou gratuits.\n \n ") 

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
    print( " Choisissez parmis les propositions suivantes : \n ")

    while True:
        user_input = input(" Vous pouvez modifier l'ordre en définissant le paramètre orderBy sur l'une des valeurs suivantes: .\n \n relevance : renvoie les résultats par ordre de pertinence des termes de recherche (valeur par défaut). \n \n newest : renvoie les résultats dans l'ordre de publication, du plus récent au moins récent. \n \n ").strip().lower()

        if user_input.strip() == "":
            print("Ce champ est obligatoire")
                

        elif user_input  not in ["relevance", "newest"]:
            print("Veuillez entrer relevance ou newest")
            
        else :
            parameters['orderBy'] = user_input
            return parameters

def get_data( url= 'https://www.googleapis.com/books/v1/volumes'):

    """
    Interroge l'API Google Books en construisant dynamiquement les paramètres
    selon les choix de l'utilisateur, puis renvoie les données brutes en format JSON.

    Étapes :
    - Appelle plusieurs fonctions pour collecter les paramètres utilisateur (recherche, filtres, etc.)
    - Envoie une requête HTTP GET à l'API Google Books avec ces paramètres
    - Vérifie le code de statut de la réponse
    - Affiche l'URL finale utilisée
    - Renvoie les données JSON de la réponse

    Paramètres :
    ----------
    url : str, optionnel
        L'URL de base de l'API Google Books (défaut : 'https://www.googleapis.com/books/v1/volumes')

    Retour :
    -------
    dict :
        Données brutes (JSON) retournées par l'API Google Books
    """
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


def data_to_dataframe(data_books):
    
    """
    Transforme les données JSON récupérées de l'API Google Books en un DataFrame Pandas.

    Paramètres
    ----------
    data_books : dict
        Données brutes issues de l'API Google Books (résultat de .json()).

    Retour
    ------
    df_books : pandas.DataFrame
        DataFrame contenant les colonnes suivantes :
        - 'title' : titre du livre
        - 'price' : prix du livre (si disponible)
        - 'rating' : note moyenne (si disponible)
    """
    data_books = data_books.get("items", [])

    # Création d'une liste de dictionnaires pour les livres
    books_list = []

    for item in data_books: 
        title = item.get("volumeInfo", []).get("title", [])
        price = item.get("saleInfo", {}).get("listPrice", {}).get("amount")
        rating = item.get("volumeInfo", {}).get("averageRating")

        book_dict = {
            "title" : title,
            "price" : price,
            "rating" : rating
        }

        books_list.append(book_dict)

    # Créer un dataframe à partir de la liste de dictionnaires
    df_books = pd.DataFrame(books_list)

    return df_books

