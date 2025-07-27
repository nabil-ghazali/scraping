# Importer les bibliothèques nécessaires
import requests
import json
import pandas as pd


def filter_data(df_books):
    """
    Filtre un DataFrame de livres pour ne conserver que ceux qui ont des valeurs
    non nulles pour les colonnes 'price' et 'rating'. 

    Ensuite, réinitialise l'index du DataFrame filtré et ajoute une colonne 'availability'
    initialisée à False.

    Paramètres
    ----------
    df_books : pandas.DataFrame
        DataFrame contenant les informations des livres, avec au moins les colonnes
        'price' et 'rating'.

    Retour
    ------
    pandas.DataFrame
        Un DataFrame filtré et nettoyé, avec un index réinitialisé et une colonne
        'availability' ajoutée à False.
    """

    # Supprime les lignes où 'price' ou 'rating' est manquant (NaN)
    df_books_filtered = df_books.dropna(subset=["price", "rating"])

    # Réinitialise l'index du DataFrame filtré pour un nouvel index continu (0, 1, 2, ...)
    df_books_new_index = df_books_filtered.reset_index(drop=True)

    # Ajoute une colonne 'availability' initialisée à False pour chaque ligne
    df_books_new_index["availability"] = False

    # Renvoie le DataFrame nettoyé et enrichi
    return df_books_new_index
